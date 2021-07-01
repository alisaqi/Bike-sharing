import main
from table import create_tables
from insert_data import create_user,create_station,check_available_origin

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
        2.stations
        3.trip

        """))
        if choice == 1:
            name = input("enter name: ")
            national_number =int(input("enter National number: "))
            lastname = input("enter Last name: ")
            birth_date =  input("plese insert your birthdate in this type :('2014-02-17')")
            gender = True if(input("please select your gender:(man or woman) ")) == 'man' else False
            create_user(dbname,national_number,name,lastname,birth_date,gender)
        elif choice == 2:
            name = input("enter station name: ")
            address_id = int(input("enter location: "))
            street_name = input("enter street name: ")
            bicycle_capacity = int(input("please enter bicycle capacity "))
            available_bicycle = int(input("please enter available bicycle "))
            # park_capacity = int(bicycle_capacity - available_bicycle)
            create_station(dbname, name, address_id, street_name, bicycle_capacity,available_bicycle)
        elif choice == 3:
            user_id = int(input("enter user id: "))
            origin_station_id = int(input("enter origin station number: "))
            check_origin = check_available_origin(dbname,origin_station_id)
            if check_origin == True:
                pass
            else:
                print("please choose another origin: ")




            #
            # origin_acceptance = True if (input("please type 'yes' if origin is accepted: ")) == 'yes' else False
            # destination_acceptance = True if (input("please type 'yes' if destination is accepted: ")) == 'yes' else False
            # destination_station_id = int(input("enter destination station number: "))
            # trip_cancel = True if (input("please type yes if trip is canceled: ")) == 'man' else False
            # trip_date =  input("plese insert trip date in this type :('2014-02-17')")
            # trip_length = int(input("enter trip lenght: "))

            # create_user(dbname, national_number, name, lastname, birth_date, gender)
    elif ans != "":
        print("\n Not Valid Choice Try again")
