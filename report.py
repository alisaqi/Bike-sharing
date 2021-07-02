from main import connect_to_DB
import main
from models import Model
import pandas as pd
import matplotlib.pyplot as plt
import psycopg2
from datetime import date


def report5(dbname):
    model = Model(dbname)
    result = model.select_query(model_name="users")
    men , women = [],[]
    for r in result:
        men.append(r) if r['gender'] == True else women.append(r)
    label = ['men','women']
    size = [len(men),len(women)]
    plt.pie(size,labels=label)
    plt.show()
def report6(dbname):
    model = Model(dbname)
    result = model.select_query(model_name="users")
    dates,ids = [],[]
    for i in result:
        dates.append(i['birthdate'])
        ids.append(i['id'])
    # print(ids[dates.index(min(dates))])

    con = psycopg2.connect(
        dbname=str(dbname),
        user='postgres',
        password='ali'
    )

    cursor = con.cursor()
    trips_oldest = "select " \
                   "trips.user_id, " \
                   "trips.origin_station_id, " \
                   "trips.destination_station_id, " \
                   "trips.trip_cancel, " \
                   "trips.trip_date, " \
                   "trips.trip_length " \
                   "from trips left join users on trips.user_id = users.id"
    cursor.execute(trips_oldest)
    rows = cursor.fetchall()

    print("Trips of Oldest user is below :\n")
    for i in rows:
        if i[0]==(ids[dates.index(min(dates))]):
            print(pd.DataFrame({
                'user id' : i[0],
                'origin station': i[1],
                'destination_station_id' : i[2],
                'destination_station_id': i[3],
                'trip_date' : i[4],
                'trip_length': [5]


    }))

    #================================


    model = Model(dbname)
    result = model.select_query(model_name="users")
    dates, ids = [], []
    for i in result:
        dates.append(i['birthdate'])
        ids.append(i['id'])
    # print(ids[dates.index(min(dates))])

    con = psycopg2.connect(
        dbname=str(dbname),
        user='postgres',
        password='ali'
    )

    cursor = con.cursor()
    trips_oldest = "select " \
                   "trips.user_id, " \
                   "trips.origin_station_id, " \
                   "trips.destination_station_id, " \
                   "trips.trip_cancel, " \
                   "trips.trip_date, " \
                   "trips.trip_length " \
                   "from trips left join users on trips.user_id = users.id"
    cursor.execute(trips_oldest)
    rows = cursor.fetchall()

    print("\nTrips of youngest user is below :\n")
    for i in rows:
        if i[0] == (ids[dates.index(max(dates))]) :
            print(pd.DataFrame({
                'user id': i[0],
                'origin station': i[1],
                'destination_station_id': i[2],
                'destination_station_id': i[3],
                'trip_date': i[4],
                'trip_length': [5]

            }))
def report4(dbname):
    price =  int(input("enter price per minute: "))
    penalty =  int(input("enter penalty per trip: "))
    model = Model(dbname)
    result = model.select_query(model_name="trips")
    profit,cancel,dates = [],[],[]
    # for i in result:
    #     if i['trip_cancel'] == True:
    #         cancel.append(1)
    #         profit.append()
    #     profit.append(int(i['trip_length'])*price )
    #     dates.append(i['trip_date'])
    for i,row in enumerate(result):
        if i == 0:
            profit.append(int(row['trip_length']) * price)
            dates.append(row['trip_date'])
        else:
            profit.append(int(row['trip_length']) * price + profit[i-1])
            dates.append(row['trip_date'])
        if row['trip_cancel'] :
            profit[i] = profit[i] - penalty
    dates.sort()
    a = pd.DataFrame({
        'date' : dates,
        'profit' : profit
    })
    a= a.sort_values('date')
    plt.plot(a['date'],a['profit'])
    plt.show()



