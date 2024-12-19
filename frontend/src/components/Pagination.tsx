import React from 'react';

interface PaginationProps {
  currentPage: number;
  totalItems: number;
  pageSize: number;
  onPageChange: (page: number) => void;
}

const Pagination: React.FC<PaginationProps> = ({ currentPage, totalItems, pageSize, onPageChange }) => {
  const totalPages = Math.ceil(totalItems / pageSize);

  if (totalPages <= 1) return null;

  const pages: number[] = [];

  for (let i = 1; i <= totalPages; i++){
    pages.push(i);
  }

  return (
    <div style={{margin: '20px 0'}}>
      {pages.map(p => (
        <button 
          key={p} 
          onClick={() => onPageChange(p)}
          style={{margin: '0 5px', fontWeight: p === currentPage ? 'bold' : 'normal'}}
        >
          {p}
        </button>
      ))}
    </div>
  );
}

export default Pagination;
