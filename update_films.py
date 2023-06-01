from connectSQL import *
from read_films import *

def film_update():
    
    id_field = int(input("Enter the ID of the desired movie to be updated."))
    field_name = input("Enter the field you wish to update. Choose from:\n Title.\n Year Released.\n Rating.\n Duration.\n Genre.\n")
    field_value = input(f"Enter the value you wish to add for the {field_name} field.\n Input MUST adhere to strict content rules.\n For rating, please enter either G, PG or R.\n For Genre, please enter either Action, Animation, Comedy, Crime, Fantasy, Fighting, Scifi, Test. ")

    match field_name:
        
        case 'title':
            field_value = field_value.title()
            
        case 'rating':
            field_value = field_value.upper()
            
        case 'genre':
            field_value = field_value.title()
            
    field_value = " ' " + field_value + " ' "

    cursor.execute(f"Update tblFilms Set {field_name} = {field_value} Where filmID = {id_field}")
    conn.commit()
    
    print(f"Record {id_field} updated in the tblFilms table.")

    read()
    
if __name__ == '__main__':
    film_update()