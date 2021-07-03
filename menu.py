import main
from table import create_tables
from insert_data import create_user,create_station,check_available_origin,suggest_origin,check_available_destination,suggest_destination,create_data_to_trip,update_capacities
from report import report5,report4,report6


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
        0.return

        """))
        if choice == 1:
            name = input("enter name: ")
            national_number =int(input("enter National number: "))
            lastname = input("enter Last name: ")
            birth_date =  str(input("plese insert your birthdate in this type (2014-02-15): "))
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
            trip_cancel = False
            origin_acceptance = False
            user_id = int(input("enter user id: "))
            origin_station_id = int(input("enter origin station number: "))
            check_origin = check_available_origin(dbname,origin_station_id)
            if check_origin == True:
                origin_acceptance = True
                origin_acceptance = True
            else:

                print("please choose another origin: ")
                list_suggusted_origins = suggest_origin(dbname,origin_station_id)
                try:
                    list_suggusted_origins.remove(origin_station_id)
                except:
                    pass
                print(list_suggusted_origins)
                print("choose one of these above: ")
                choosen_suggested_origin = int(input())
                if choosen_suggested_origin  not in list_suggusted_origins:
                    choosen_suggested_origin= int(input("choose right station id, otherwise you don't like any of them type 0: "))
                    if choosen_suggested_origin == 0:
                        trip_cancel = True


                    # else:
                    #     origin_acceptance = False
                elif choosen_suggested_origin  in list_suggusted_origins:
                    origin_acceptance = False


            destination_acceptance = 0
            destination_station_id = int(input("enter destination station number: "))
            check_destination = check_available_destination(dbname, destination_station_id)
            if check_destination == True:
                destination_acceptance = True
            else:

                print("please choose another destination: ")
                list_suggusted_destination = suggest_destination(dbname, destination_station_id)
                list_suggusted_destination.remove(destination_station_id)
                print(list_suggusted_destination)
                print("choose one of these above: ")
                choosen_suggested_destination = int(input())
                if choosen_suggested_destination  not in list_suggusted_destination:
                    choosen_suggested_destination = int(input("choose right station id, otherwise you don't like any of them type 0: "))
                    if choosen_suggested_destination == 0:
                        trip_cancel = True
                    # else:
                    #     destination_acceptance = False
                elif choosen_suggested_destination  in list_suggusted_destination:
                    destination_acceptance = False

            # cancel = int(input("Is trip Accepted ? (Type 1 if yes, type 0 if NO)"))
            trip_length = 0
            trip_date = input("enter trip date in this form (2020-04-10): ")
            # if cancel == 1:
            #     trip_cancel = False
            # else:
            #     trip_cancel = True
            if trip_cancel is False:
                trip_length = int(input("please enter trip lenght in minutes: "))
            else:
                pass
            create_data_to_trip(dbname,user_id,origin_station_id,origin_acceptance,destination_acceptance,destination_station_id,trip_cancel,trip_date,trip_length = trip_length)

            if trip_cancel is False:
                update_capacities(dbname,origin_station_id, destination_station_id)
                print("data is created")
            else:
                pass

            # elif choice == 0:
            #     exit(choice)
    elif  ans == "4":
        answer = True
        while answer != "0":
            print("""
            1.report 1
            2.report 2
            3.report 3
            4.report 4
            5.report 5
            6.report 6
            0.RETURN

            """)
            answer = input("Which report would you like to see? ")
            if answer == "5":
                report5(dbname)
            elif answer == "6":
                report6(dbname)
            elif  answer == "4":
                report4(dbname)
            elif answer == "3":
                print("OUT OF SERVICE :)))))))))))))")
            elif answer == "2":
                print("OUT OF SERVICE :)))))))))))))")
            elif answer == "1":
                print("OUT OF SERVICE :)))))))))))))")
            elif answer == "0":
                answer == "0"

    elif ans != "":
        print("\n Not Valid Choice Try again")
