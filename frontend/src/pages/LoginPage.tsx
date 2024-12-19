import React, { useState } from 'react';
import { login } from '../utils/api.tsx';

const LoginPage: React.FC = () => {
  const [username, setUsername] = useState<string>('');
  const [password, setPassword] = useState<string>('');
  const [error, setError] = useState<string>('');

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    try {
      const data = await login(username, password);
      localStorage.setItem('token', data.access_token);
      window.location.href = '/admin';
    } catch (err) {
      setError('Неправильный логин или пароль');
    }
  }

  return (
    <div>
      <h1>Вход</h1>
      {error && <p style={{color:'red'}}>{error}</p>}
      <form onSubmit={handleSubmit}>
        <input value={username} onChange={e => setUsername(e.target.value)} placeholder="Логин" />
        <input type="password" value={password} onChange={e => setPassword(e.target.value)} placeholder="Пароль" />
        <button type="submit">Войти</button>
      </form>
    </div>
  );
}

export default LoginPage;
