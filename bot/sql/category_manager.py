class Category():

    def __init__(self, cursor):
        self.cursor = cursor


    def create_table(self):
    # Создает таблицу категорий
        query = """
        CREATE TABLE IF NOT EXISTS category(
        id INTEGER PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(50) NOT NULL UNIQUE
            );
        """
        result = self.cursor.execute(query)
        return result

    def add_new_category(self, name):
        # Добавляет новую категорию
      
        query = f"""
            INSERT INTO category(name) VALUES('{name}');
        """
        result = self.cursor.execute(query)
        return result

    def delete_category(self, id):
   
        query = f"""
            DELETE FROM category WHERE id={id};
        """
        result = self.cursor.execute(query)
        return result

    def update_category(self, id, new_value):

        query = f"""
            UPDATE category SET name='{new_value}' WHERE id={id};
        """
        result = self.cursor.execute(query)
        return result
    
    def get_all_categories(self):
        query = f"""
            SELECT * FROM category;
        """
        result = self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_category_by_name(self, name):
        query = f"""
            SELECT * FROM category WHERE name='{name}';
        """
        self.cursor.execute(query)
        return self.cursor.fetchone()