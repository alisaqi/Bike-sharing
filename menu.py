import main
from table import create_tables
from insert_data import create_user

dbname = 'mis_9612743155'
ans = True
while ans:
    print("""
    1.create database
    2.create table
    3.write data
    4.report
    """)
    ans = input("What would you like to do? ")

    if ans == "1":
        dbname = input("enter db name: ")
        cursor,con = main.connect()
        dbname = main.CreateDB(cursor,con,dbname)
    elif ans == "2":
        create_tables(dbname)
    elif ans == "3":
        choice = int(input("""
        1.user
        2.trip
        3.stations
        """))
        if choice == 1:
            name = input("enter name: ")
            national_number =int(input("enter National number: "))
            lastname = input("enter Last name: ")
            birth_date =  '2014-02-17'
            gender = True if(input("enter name: ")) == 'true' else False
            create_user(dbname,national_number,name,lastname,birth_date,gender)
        elif choice == 2:
            pass
    # elif ans == "4":
    #     print("\n Goodbye")
    elif ans != "":
        print("\n Not Valid Choice Try again")
