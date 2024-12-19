import asyncio
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.routers import products, admin, auth
from app.middlewares.error_handler import register_error_handler
from app.database import Base, engine, get_db
from sqlalchemy.orm import Session
from app.models import User
from app.core.security import get_password_hash
import sys
import os


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Асинхронная функция для инициализации при старте
    def startup_tasks():
        # Создание таблиц, если они ещё не созданы
        Base.metadata.create_all(bind=engine)

        # Получение сессии базы данных
        db = next(get_db())

        # Проверка наличия администратора
        admin_username = "ann"
        admin_password = "123Ann"
        admin_user = db.query(User).filter(User.username == admin_username).first()
        if not admin_user:
            # Хеширование пароля
            hashed_password = get_password_hash(admin_password)

            # Создание администратора
            admin_user = User(username=admin_username, hashed_password=hashed_password, role="admin")
            db.add(admin_user)
            db.commit()
            db.refresh(admin_user)
            print(f"Администратор '{admin_username}' успешно создан.")
        else:
            print(f"Администратор '{admin_username}' уже существует.")

    # Запуск инициализационных задач в отдельном потоке
    await asyncio.to_thread(startup_tasks)

    # Yield control обратно приложению
    yield

    # Здесь можно добавить задачи при завершении работы, если необходимо
    # Например, закрыть соединения, очистить ресурсы и т.д.


# Создание экземпляра FastAPI с lifespan обработчиком
app = FastAPI(
    title="Knife Store API",
    lifespan=lifespan
)

# Подключение статических файлов
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Добавление CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # В продакшене рекомендуется ограничить источники
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Регистрация обработчиков ошибок
register_error_handler(app)

# Подключение роутеров
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(products.router, prefix="/api/products", tags=["products"])
app.include_router(admin.router, prefix="/api/admin", tags=["admin"])

# База данных инициализируется через lifespan обработчик
