from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Cookie_order:
    DB = 'cookie_orders'

    def __init__(self , cookie_order):
        self.id = cookie_order['id']
        self.name = cookie_order['name']
        self.cookie_type = cookie_order['cookie_type']
        self.num_boxes = cookie_order['num_boxes']
        self.created_at = cookie_order['created_at']
        self.updated_at = cookie_order['updated_at']

    @classmethod
    def is_valid(cls, cookie_order):
        valid = True
        print(cookie_order)
        if len(cookie_order['name'])<1 or len(cookie_order['cookie_type'])<1 or int(cookie_order['num_boxes'])<1:
            valid = False
            flash("All Fields Required")
            return valid
        if len(cookie_order['name'])<2:
            valid = False
            flash("Customer Name must be at least 2 characters")
        if len(cookie_order['cookie_type'])<2:
            valid = False
            flash("Cookie Type must be at least 2 characters")
        if len(cookie_order['num_boxes'])<0:
            valid = False
            flash("Order must be at least 1 box")
        return valid

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM cookie_orders;"
        orders_data = connectToMySQL(cls.DB).query_db(query)
        orders = []
        for order in orders_data:
            orders.append(cls(order))
        return orders
    
    @classmethod
    def get_by_id(cls, order_id):
        query = """
                SELECT * FROM cookie_orders
                WHERE id = %(id)s;
        """
        data = {
            "id":order_id
        }
        result = connectToMySQL(cls.DB).query_db(query, data)
        if result:
            order = result[0]
            return order
        return False
    
    @classmethod
    def create(cls,cookie_order):
        query = """
            INSERT into cookie_orders (name, cookie_type, num_boxes)
            VALUES (%(name)s, %(cookie_type)s, %(num_boxes)s);
        """
        results = connectToMySQL(cls.DB).query_db(query, cookie_order)
        return results
    
    @classmethod
    def update(cls,cookie_order):
        query = """
            UPDATE cookie_orders
            SET name = %(name)s, cookie_type = %(cookie_type)s, num_boxes = %(num_boxes)s
            WHERE id = %(id)s;
        """
        results = connectToMySQL(cls.DB).query_db(query, cookie_order)
        return results
    
    @classmethod
    def delete(cls, cookie_order):
        query = "DELETE FROM cookie_orders WHERE id = %(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, cookie_order)
        return results

#     @classmethod
#     def save(cls, data):
#         query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW());"
#         # data is a dictionary that will be passed into the save method from server.py
#         return connectToMySQL('users_schema').query_db(query, data)
