import React from 'react';
import { Link } from 'react-router-dom';

import {Product } from '../types/types.tsx';

interface ProductCardProps {
  product: Product;
}

const ProductCard: React.FC<ProductCardProps> = ({ product }) => {
  const image = product.images && product.images.length > 0 ? product.images[0] : 'placeholder.jpg';

  return (
    <div style={{
      border: '1px solid #ccc',
      margin: '10px',
      padding: '10px',
      width: '200px'
    }}>
      <Link to={`/product/${product.id}`}>
        <img src={image} alt={product.name} style={{width: '100%'}} />
        <h3>{product.name}</h3>
      </Link>
      <p>Цена: {product.price}</p>
    </div>
  );
}

export default ProductCard;
