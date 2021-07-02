from main import connect_to_DB
import main

dbname = 'mis_9612743155' #input("enter db name: ")
cursor,con = main.connect()

ans = True
while ans:
    print("""
    1.report 1
    2.report 2
    3.report 3
    4.report 4
    5.report 5
    6.report 6
    
    """)
    ans = input("Which report would you like to see? ")
    if ans == 1:
        # report1 = "SELECT trips.origin_station_id, Count(trips.origin_station_id) AS CountOforigin_station_id, trips.trip_cancel FROM trips GROUP BY trips.origin_station_id, trips.trip_cancel HAVING (((trips.trip_cancel)=None));"
        # cursor.exexute(report1)
        report1 = 'select * from trips'
        cursor.exexute(report1)
        print(report1)
        for i in report1:
            print(i)
        # print(report1)