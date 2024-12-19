import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { getProductById } from '../utils/api.tsx';
import { Product } from '../types/types.tsx';

const ProductPage: React.FC = () => {
  const { id } = useParams<{ id: string }>();
  const [product, setProduct] = useState<Product | null>(null);

  useEffect(() => {
    async function fetchData() {
      if (!id) return;
      const data: Product = await getProductById(parseInt(id, 10));
      setProduct(data);
    }
    fetchData();
  }, [id]);

  if (!product) return <div>Загрузка...</div>;

  return (
    <div>
      <h1>{product.name}</h1>
      {product.images && product.images.map((img, idx) => (
        <img key={idx} src={img} alt={product.name} style={{width: 200, marginRight: 10}} />
      ))}
      <p>{product.description}</p>
      <ul>
        <li>Цена: {product.price}</li>
      </ul>
    </div>
  );
}

export default ProductPage;
