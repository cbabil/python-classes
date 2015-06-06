"""
Create the animal and food table.
Populate both tables with data
"""

def drop_table(db, tbl):
    cursor = db.cursor()
    for table in tbl:
        cursor.execute("""DROP TABLE IF EXISTS %s""" % table)

    cursor.close()
    print("All Table dropped")

def create_animal(db):
    cursor = db.cursor()
    cursor.execute("""
        CREATE TABLE animal (
            id INTEGER PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(20),
            family VARCHAR(50),
            weight INTEGER)
        """)

    data = (
            ("Ellie", "Elephant", 2350),
            ("Gerald", "Gnu", 1400),
            ("Gerald", "Giraffe", 940),
            ("Leonard", "Leopard", 280),
            ("Sam", "Snake", 24),
            ("Steve", "Snake", 35),
            ("Zorro", "Zebra", 340),
            ("NoFood", "Tiger", 350)
            )
    
    cursor.execute("DELETE FROM animal")
    for animal in data:
        cursor.execute("""
            INSERT INTO animal (name, family, weight) 
            VALUES (%s, %s, %s)
        """, animal)
    
    db.commit()
    cursor.close()
    print("Animal Table Created and Populated with data")

def create_food(db):
    cursor = db.cursor()
    cursor.execute("""
        CREATE TABLE food (
            id INTEGER PRIMARY KEY AUTO_INCREMENT,
            anid INTEGER,
            feed VARCHAR(20),
            FOREIGN KEY (anid) REFERENCES animal(id))
    """)

    data = [('Ellie', 'Elephant', ['hay', 'peanuts']),
        ('Gerald', 'Gnu', ['leaves', 'shoots']),
        ('Gerald', 'Giraffe', ['hay', 'grass']),
        ('Leonard', 'Leopard', ['meat']),
        ('Sam', 'Snake', ['mice', 'meat']),
        ('Steve', 'Snake', ['mice', 'meat']),
        ('Zorro', 'Zebra', ['grass', 'leaves']),
        ('NoFood', 'Tiger', [])
    ]

    for name, family, foods in data:
        cursor.execute("SELECT id FROM animal WHERE name=%s and family=%s",
                (name, family))
        try:
            animal_id = cursor.fetchone()[0]
            for food in foods:
                cursor.execute("""INSERT INTO food (anid, feed) 
                    VALUES (%s, %s)""", (animal_id, food))
        except TypeError: 
            print('Name: %s or Family: %s does not exists in animal table' % (name, family))
    db.commit()
    cursor.close()
    print("Food Table Created and Populated with data")

if __name__ == "__main__":
    import mysql.connector
    from database import login_info

    table = ['food', 'animal']
    database = mysql.connector.Connect(**login_info)

    # Drop table if exists
    drop_table(database, table)

    # Create Animal table
    create_animal(database)

    # Create Food table
    create_food(database)