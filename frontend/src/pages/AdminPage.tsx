import React, { useEffect, useState } from 'react';
import { getProducts, deleteProduct } from '../utils/api.tsx';
import {ProductsResponse, Product } from '../types/types.tsx';


const AdminPage: React.FC = () => {
  const [products, setProducts] = useState<Product[]>([]);

  useEffect(() => {
    async function fetchData() {
      const data: ProductsResponse = await getProducts(1);
      setProducts(data.data);
    }
    fetchData();
  }, []);

  async function handleDelete(id: number) {
    await deleteProduct(id);
    setProducts(products.filter(p => p.id !== id));
  }

  return (
    <div>
      <h1>Админка</h1>
      <ul>
        {products.map(p => (
          <li key={p.id}>
            {p.name} 
            <button onClick={() => handleDelete(p.id)}>Удалить</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default AdminPage;
