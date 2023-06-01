from connectSQL import *

cursor.execute(
    """
    USE tblFilms;
    Create Table IF NOT EXISTS tblFilms (
        "filmID" Integer Not Null Unique,
        "title" Text,
        "yearReleased" Integer,
        "rating" Text,
        "duration" Integer,
        "genre" Text,
        Primary Key("filmID" AutoIncrement)
    )
    """
)