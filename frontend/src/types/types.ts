export interface Product {
    id: number;
    name: string;
    price: number;
    description: string | undefined;
    images?: string[];
  }
  
  
  export interface ProductsResponse {
    data: any[];
    total: number;
    page: number;
  }