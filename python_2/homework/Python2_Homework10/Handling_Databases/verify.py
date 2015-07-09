import mysql.connector
from database import login_info

def verify_animal(db):
    '''
    Verifies that every animal in the "animal" table eats 
    at least one food from the "food" table.
    '''
    cursor = db.cursor()
    cursor.execute("SELECT * FROM animal WHERE id NOT IN (SELECT anid FROM food)")
    animals = cursor.fetchall()
    cursor.close()
    
    return animals

if __name__ == "__main__":
    database = mysql.connector.Connect(**login_info)
    animals = verify_animal(database)
    if animals:
        for animal in animals:
            print("{}, the {} has no food to eat".format(animal[1],animal[2]))
    else:
        print("Every animal eats at least one food")