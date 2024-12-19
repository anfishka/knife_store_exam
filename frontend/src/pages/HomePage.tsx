import React, { useEffect, useState } from 'react';
import { getProducts } from '../utils/api.tsx';
import ProductCard from '../components/ProductCard.tsx';
import Pagination from '../components/Pagination.tsx';
import {ProductsResponse, Product } from '../types/types.tsx';

const HomePage: React.FC = () => {
  const [products, setProducts] = useState<Product[]>([]);
  const [total, setTotal] = useState<number>(0);
  const [page, setPage] = useState<number>(1);
  const pageSize = 12;

  useEffect(() => {
    async function fetchData() {
      const data: ProductsResponse = await getProducts(page);
      setProducts(data.data);
      setTotal(data.total);
    }
    fetchData();
  }, [page]);

  return (
    <div>
      <h1>Список карманных ножей</h1>
      <div style={{display: 'flex', flexWrap: 'wrap'}}>
        {products.map(p => (
          <ProductCard key={p.id} product={p} />
        ))}
      </div>
      <Pagination
        currentPage={page}
        totalItems={total}
        pageSize={pageSize}
        onPageChange={setPage}
      />
    </div>
  );
}

export default HomePage;
