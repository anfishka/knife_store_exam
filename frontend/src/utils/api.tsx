import axios from 'axios';
import {ProductsResponse, Product } from '../types/types.tsx';

//const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api';

const API_URL = 'http://localhost:5050/api';


interface LoginResponse {
  access_token: string;
}




export async function getProducts(page: number = 1): Promise<ProductsResponse> {
  const res = await axios.get(`${API_URL}/products?page=${page}`);
  return res.data;
}

export async function getProductById(id: number): Promise<Product> {
  const res = await axios.get(`${API_URL}/products/${id}`);
  return res.data;
}

export async function login(username: string, password: string): Promise<LoginResponse> {
  const res = await axios.post(`${API_URL}/auth/login`, { username, password });
  return res.data;
}

export async function deleteProduct(id: number): Promise<void> {
  const token = localStorage.getItem('token');
  await axios.delete(`${API_URL}/admin/products/${id}`, {
    headers: {
      Authorization: `Bearer ${token}`
    }
  });
}
