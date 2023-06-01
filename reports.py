from connectSQL import *

def read_report():
    
    reports_on = True
    
    while reports_on:
        report_options = input("FilmFlix Database / tblFilms Table / Reports\n To view a report from this database, enter an option by number:\n1. View all records in a selected column.\n2. View all films within a selected genre.\n3. View all films released in a selected year.\n4. View all films with a selected rating.\n5. Exit to Main Menu.\n")

        ops_flag = True
        
        while ops_flag:
            
            match report_options:
                
                case '1':
                    column_view = input("Select a column to view all records from. Enter your choice by letter.:\nA. Title.\nB. Year Released\nC. Rating.\nD. Duration.\nE. Genre.\n")

                    column_view = column_view.upper()
                    
                    match column_view:
                        case 'A':
                            cursor.execute("Select Title from tblFilms")
                            column = cursor.fetchall()
                            
                            for field in column:
                                print(field)

                        case 'B':
                            cursor.execute("Select Year Released from tblFilms")
                            column = cursor.fetchall()
                            
                            for field in column:
                                print(field)
                                
                        case 'C':
                            cursor.execute("Select Rating from tblFilms")
                            column = cursor.fetchall()
                            
                            for field in column:
                                print(field)
                        
                        case 'D':
                            cursor.execute("Select Duration from tblFilms")
                            column = cursor.fetchall()
              
                            for field in column:
                                print(field)
                                
                        case 'E':
                            cursor.execute("Select Genre from tblFilms")
                            column = cursor.fetchall()
                            
                            for field in column:
                                print(field)
                    
                    ops_flag = False
                
                case '2':
                    
                    genre_view = input("To view all films with a specific Genre - Enter desired genre:\n Action.\n Animation.\n Comedy.\n Crime.\n Fantasy.\n Fighting.\n Scifi.\n Test.")

                    genre_view = genre_view.lower()
                    
                    match genre_view:
                        
                        case 'action':
                            cursor.execute("Select * From tblFilms Where genre = \'Action\'")
                            row = cursor.fetchall()
                            
                            for record in row:
                                print(record)
                                
                        case 'animation':
                            cursor.execute("Select * From tblFilms Where genre = \'Animation\'")
                            row = cursor.fetchall()
                            
                            for record in row:
                                print(record)

                        case 'comedy':
                            cursor.execute("Select * From tblFilms Where genre = \'Comedy\'")
                            row = cursor.fetchall()
                            
                            for record in row:
                                print(record) 
                        
                        case 'crime':
                            cursor.execute("Select * From tblFilms Where genre = \'Crime\'")
                            row = cursor.fetchall()
                            
                            for record in row:
                                print(record) 
                        
                        case 'fantasy':
                            cursor.execute("Select * From tblFilms Where genre = \'Fantasy\'")
                            row = cursor.fetchall()
                            
                            for record in row:
                                print(record)
                        
                        case 'fighting':
                            cursor.execute("Select * From tblFilms Where genre = \'Fighting\'")
                            row = cursor.fetchall()
                            
                            for record in row:
                                print(record)
                                
                        case 'scifi':
                            cursor.execute("Select * From tblFilms Where genre = \'Scifi\'")
                            row = cursor.fetchall()
                            
                            for record in row:
                                print(record)
                        
                        case 'test':
                            cursor.execute("Select * From tblFilms Where genre = \'Test\'")
                            row = cursor.fetchall()
                            
                            for record in row:
                                print(record)
                                
                    ops_flag = False
                    
                case '3':
                    
                    year_choice = input("To view all films released in a specific year, Enter desired year.")
                    year_choice = " ' " + year_choice + " ' "
                    cursor.execute(f"Select * From tblFilms Where yearReleased = {year_choice}")
                    row - cursor.fetchall()
                    
                    for record in row:
                        print(record)

                    ops_flag = False
                    
                case '4':
                    
                    rating_view = input("To view all films with a specific rating, Enter an option via its code:\n G. General Audience.\n PG. Parental Guidance.\n R. Restricted.")
                    rating_view = rating_view.upper()
                    
                    match rating_view:
                        
                        case 'G':
                            cursor.execute("Select * From tblFilms Where rating = \'G\'")
                            row = cursor.fetchall()
                            
                            for record in row:
                                print(record)
                                
                        case 'PG':
                            cursor.execute("Select * From tblFilms Where rating = \'PG\'")
                            row = cursor.fetchall()
                            
                            for record in row:
                                print(record)
                                
                        case 'R':
                            cursor.execute("Select * From tblFilms Where rating = \'R\'")
                            row = cursor.fetchall()
                            
                            for record in row:
                                print(record)
                                
                    ops_flag = False
                    
                case '5':
                    
                    print("You have Exited Reports.")
                    
                    ops_flag = False
                    report_options = False
                    
                case _:
                    
                    print(f"{report_options} is not a valid input. Please select a valid input.")
                    
                    report_options = input("FilmFlix Database / tblFilms Table / Reports\n To view a report from this database, enter an option by number:\n View all records in a selected column\n2. View all films within a selected genre\n3. View all films released in a selected year\n4. View all films with a selected rating\n5. Exit to Main Menu.\n")

if __name__ == '__main__':
    read_report()
                
        