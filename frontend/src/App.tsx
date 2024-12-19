import React from 'react';
import { Routes, Route } from 'react-router-dom';
import HomePage from './pages/HomePage.tsx';
import ProductPage from './pages/ProductPage.tsx';
import AdminPage from './pages/AdminPage.tsx';
import LoginPage from './pages/LoginPage.tsx';

const App: React.FC = () => {
  return (
    <div>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/product/:id" element={<ProductPage />} />
        <Route path="/admin" element={<AdminPage />} />
        <Route path="/login" element={<LoginPage />} />
      </Routes>
    </div>
  );
}

export default App;
