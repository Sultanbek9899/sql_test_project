class Product():
    
    def __init__(self, cursor):
        self.cursor = cursor

    
    def _execute_query(self, query):
        result = self.cursor.execute(query)
        # Выполняетя команда  в базу
        return
    
    def create_product_table(self):
        query = """
            CREATE TABLE IF NOT EXISTS product(
                id INTEGER PRIMARY KEY AUTO_INCREMENT,
                name VARCHAR(255) NOT NULL,
                description TEXT, 
                price DECIMAL(10,2) NOT NULL,
                    is_available BOOLEAN NOT NULL DEFAULT true, 
                    category_id INTEGER NOT NULL, 
                    FOREIGN KEY(category_id) REFERENCES category(id)
                );
        """
        res = self._execute_query(query)
        return res


    def add_product(self, data):
        query = f"""
            INSERT INTO product(
                name, description, price, category_id)
            VALUES('{data.get("name")}', '{data.get("description")}',
                {data.get('price')}, {data.get('category_id')}
            );
        """
        self._execute_query(query)
    
    def get_all_products(self):
        query = """
            SELECT * FROM product;
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def get_products_by_category(self, category_id):
        query = f"""
            SELECT * FROM product WHERE category_id={category_id};
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def get_product_by_id(self,id):
        query = f"""
            SELECT * FROM product WHERE id={id};
        """
        self.cursor.execute(query)
        return self.cursor.fetchone()
    
    def _get_all_ids(self):
        query = f"""
            SELECT id FROM product;
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()
    