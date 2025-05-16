import sqlite3

try:
    with sqlite3.connect("../db/lesson.db") as conn:
        cursor = conn.cursor()
        conn.execute("PRAGMA foreign_keys = 1")
        #Task 1: Complex JOINs with Aggregation
        print("\nTask 1:")
        query = """
            SELECT o.order_id, SUM(p.price * l.quantity) AS total_price
            FROM orders o
            JOIN line_items l ON o.order_id = l.order_id
            JOIN products p ON l.product_id = p.product_id
            GROUP BY o.order_id
            ORDER BY o.order_id
            LIMIT 5;
        """
        cursor.execute(query)
        results = cursor.fetchall()
        for r in results:
            print(r)


        #Task 2: Understanding Subqueries
        print("\nTask 2:")
        query2 = """
        SELECT c.customer_name, AVG(subquery.total_price) AS average_total_price
        FROM customers c
        LEFT JOIN (
            SELECT o.customer_id AS customer_id_b, SUM(p.price * l.quantity) AS total_price
            FROM orders o
            JOIN line_items l ON o.order_id = l.order_id
            JOIN products p ON l.product_id = p.product_id
            GROUP BY o.order_id
            ) AS subquery
        ON c.customer_id =subquery.customer_id_b
        GROUP BY c.customer_id;             
        """
        cursor.execute(query2)
        results2 = cursor.fetchall()
        for r in results2:
            print(r)


        #Task 3: An Insert Transaction Based on Data
        print("\nTask 3:")
        #Get an employee_id
        cursor.execute("SELECT employee_id FROM employees WHERE first_name = 'Miranda' AND last_name = 'Harris';")
        employee_id = cursor.fetchone()[0]
        #Get customer_id
        cursor.execute("SELECT customer_id FROM customers WHERE customer_name = 'Perez and Sons';")
        customer_id = cursor.fetchone()[0]
        #Get the product_ids of the 5 least expensive products
        cursor.execute("SELECT product_id FROM products ORDER BY price LIMIT 5;")
        product_ids = [row[0] for row in cursor.fetchall()]

        #Create a transaction to add an order record and the 5 line_item records comprising the order
        try:
            conn.execute("BEGIN")
            cursor.execute("""
            INSERT INTO orders (customer_id, employee_id)
            VALUES (?,?)
            RETURNING order_id           
            """, (customer_id, employee_id))
            order_id =  cursor.fetchone()[0]
            for product_id in product_ids:
                cursor.execute("""
                INSERT INTO line_items(order_id, product_id, quantity)
                VALUES (?,?,?)
                """, (order_id, product_id, 10))
            conn.commit()

            #Print out order items
            cursor.execute("""
            SELECT l.line_item_id, l.quantity, p.product_name
            FROM line_items l
            JOIN products p
            ON l.product_id = p.product_id
            WHERE l.order_id = ?            
            """, (order_id,))
            order_results = cursor.fetchall()
            for row in order_results:
                print(row)
        except Exception as e:
            conn.rollback()
            print("Error:", e)

        #Task 4: Aggregation with HAVING
        print("\nTask 4:")
        query3 = """SELECT e.employee_id, e.first_name, e.last_name, count(o.order_id) AS orders_count
                    FROM employees e
                    JOIN orders o
                    ON e.employee_id = o.employee_id
                    GROUP BY e.employee_id
                    HAVING count(o.order_id) > 5;
                """
        cursor.execute(query3)
        results3 = cursor.fetchall()
        for r in results3:
            print(r)

except sqlite3.Error as e:
    print(f"An error occurred while working with the database: {e}")



