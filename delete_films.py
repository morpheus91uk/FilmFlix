from connectSQL import *
from read_films import *
import time

def film_delete():
    id_field = int(input("Enter the filmID of the record you wish to delete."))

    cursor.execute(f"Delete From tblFilms Where filmID = {id_field}")
    conn.commit()
    
    print(f"filmID {id_field} has been succesfully delted from the tblFilms table.")

    read()
    
if __name__ == '__main__':
    film_delete()    