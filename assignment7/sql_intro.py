import sqlite3

def add_publisher(cursor, name):
    try:
        cursor.execute("INSERT INTO publishers (name) VALUES (?)", (name,))
    except sqlite3.IntegrityError:
        print(f"'{name}' is already in the database.") 
    except sqlite3.Error as e:
        print(f"An error occurred while adding a publisher: {e}")

def add_magazine(cursor, name,publisher_name):
    try:
        cursor.execute("SELECT id FROM publishers WHERE name = ?", (publisher_name,))
        publisher_id = cursor.fetchone()
        if publisher_id:
            try:
                cursor.execute("INSERT INTO magazines (name, publisher_id) VALUES (?,?)", (name, publisher_id[0]))
            except sqlite3.IntegrityError:
                print(f"{name} is already in the database.")
        else:
            print(f"Publisher '{publisher_name}' not found.")
    except sqlite3.Error as e:
        print(f"An error occurred while adding a magazine: {e}")

def add_subscriber(cursor, name, address):
    try:
        cursor.execute("SELECT id FROM subscribers WHERE name = ? AND address = ?", (name, address))
        if cursor.fetchone():
            print(f"Subscriber '{name}' with '{address}' already exists.")
        else:
            cursor.execute("INSERT INTO subscribers (name, address) VALUES (?, ?)", (name, address))
    except sqlite3.Error as e:
        print(f"An error occurred while adding a subscriber: {e}")

def add_subscription(cursor, subscriber_name, subscriber_address, magazine_name, expiration_date):
    try: 
        cursor.execute("SELECT id FROM subscribers WHERE name = ? AND address = ?", (subscriber_name, subscriber_address))
        subscriber_result = cursor.fetchone()

        cursor.execute("SELECT id FROM magazines WHERE name = ?", (magazine_name,))
        magazine_result = cursor.fetchone()

        if subscriber_result and magazine_result:
            try: 
                cursor.execute("""
                    INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date) 
                    VALUES (?, ?, ?)""",
                    (subscriber_result[0], magazine_result[0], expiration_date))
            except sqlite3.IntegrityError:
                print(f"{subscriber_name} is already subscribed to '{magazine_name}'.")
        else:
            print("Subscriber or magazine not found.")
    except sqlite3.Error as e:
        print(f"An error occurred while adding a subscription: {e}") 

#Task 1: Create a New SQLite Database
try:
    with sqlite3.connect("../db/magazines.db") as conn:
        print("Database created and connected successfully.")
        conn.execute("PRAGMA foreign_keys = 1")
        cursor = conn.cursor()

        #Task 2: Define Database Structure
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS publishers (
            id INTEGER PRIMARY KEY,
            name  TEXT NOT NULL UNIQUE    
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS magazines (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            publisher_id INTEGER NOT NULL,         
            FOREIGN KEY (publisher_id) REFERENCES publishers (id)
        )
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscribers (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            address TEXT NOT NULL
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscriptions (
            id INTEGER PRIMARY KEY,
            subscriber_id INTEGER NOT NULL,
            magazine_id INTEGER NOT NULL,   
            expiration_date TEXT NOT NULL,          
            FOREIGN KEY (subscriber_id) REFERENCES subscribers (id),
            FOREIGN KEY (magazine_id) REFERENCES magazines (id)
            UNIQUE(subscriber_id, magazine_id)
        )
        """)
        
        #Task 3: Populate Tables with Data
        add_publisher(cursor, "Tax Analysts")
        add_publisher(cursor, "National Geographic Partners")
        add_publisher(cursor, "Condé Nast")
        add_publisher(cursor, "Dell Magazines")
        add_magazine(cursor, "Dell Crazy for Sudoku!", "Dell Magazines")
        add_magazine(cursor, "Dell Logic Puzzles", "Dell Magazines")
        add_magazine(cursor, "Dell Logic Puzzles", "Dell")
        add_magazine(cursor, "Vogue", "Condé Nast")
        add_magazine(cursor, "National Geographic", "National Geographic Partners")
        add_subscriber(cursor, "Alice Smith","111 Main Str, Georgetown, TX, 78645")
        add_subscriber(cursor, "Alice Smith","34 Congress Ave, Austin TX, 78645")
        add_subscriber(cursor, "Mila Smith","111 Main Str, Georgetown, TX, 78645")
        add_subscriber(cursor, "Lana Stogov","1210 Sunny Ave, Austin TX, 78600")
        add_subscription(cursor, "Alice Smith", "111 Main Str, Georgetown, TX, 78645", "Vogue", "01-01-2026")
        add_subscription(cursor, "Alice Smith", "34 Congress Ave, Austin TX, 78645", "Vogue", "01-01-2026")
        add_subscription(cursor, "Alice Smith", "34 Congress Ave, Austin TX, 78645", "Dell Crazy for Sudoku!", "12-01-2025")
        add_subscription(cursor, "Mila Smith", "111 Main Str, Georgetown, TX, 78645", "Vogue", "01-01-2026")
        add_subscription(cursor, "Lana Stogov", "111 Main Str", "Vogue", "01-01-2026")
        add_subscription(cursor, "Lana Stogov", "1210 Sunny Ave, Austin TX, 78600", "Dell Logic Puzzles", "07-01-2026")
        add_subscription(cursor, "Lana Stogov", "1210 Sunny Ave, Austin TX, 78600", "National Geographic", "02-01-2026")
        conn.commit()

        
except sqlite3.Error as e:
    print(f"An error occurred while connecting to the database: {e}")