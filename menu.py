from connectSQL import *
import read_films
import add_films
import update_films
import delete_films
import reports

def menu_options():
    
    program = True
    
    while program:
        choice_action = input("filmflix Database / tblFilms Table \n To interact with this database, Start by entering an option by number:\n1. Add Record\n2. Update Record.\n3. Delete Record\n4. View All Records.\n5. View Reports.\n6. Exit Program.\n\n ")

        flag = True
        4
        while flag:
            match choice_action:
                
                case '1':
                    add_films.film_insert()
                    flag = False
                case '2':
                    update_films.film_update()
                    flag = False
                case '3':
                    delete_films.film_delete()
                    flag = False
                case '4':
                    read_films.read()
                    flag = False
                case '5':
                    reports.read_report()
                    flag = False
                case '6':
                    print("You have no Exited the programe.")
                    flag = False
                    program = False
                case _:
                    print(f"{choice_action} is not a valid input. Please select a valid input")
                    choice_action = input("FilmFlix Database / tblFilms Table\n Enter an option by number:\n1. Add Record\n2. Update Record.\n3. Delete Record\n4. View All Records.\n 5. View Reports.\n6. Exit Program. ")

menu_options()
                