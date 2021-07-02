

def create_user(dbname,national_number,name,lastname,birth_date,gender):
    from models import Model
    model=Model(dbname=dbname)
    user = model.insert_query(model_name='users',input_array={
        'code_melli':national_number,
        'name':name,
        'last_name':lastname,
        'birthdate':birth_date,
        'gender':gender,
    })

def create_station(dbname,name,address_id,street_name,bicycle_capacity,available_bicycle):
    from models import Model
    model = Model(dbname = dbname)
    stations = model.insert_query(model_name="stations",input_array={
        'name' : name,
        'address_id' :address_id,
        'street_name' : street_name,
        'bicycle_capacity' :bicycle_capacity,
        'available_bicycle' : available_bicycle,
    })

def create_trip(dbname,user_id,origin_station_id,origin_acceptance,destination_acceptance,destination_station_id,trip_cancel,trip_date,trip_length):
    from models import Model
    model = Model(dbname = dbname)
    trips = model.insert_query(model_name="trips",input_array={
        'user_id' : user_id,
        'origin_station_id' :origin_station_id,
        'origin_acceptance' : origin_acceptance,
        'destination_acceptance' :destination_acceptance,
        'destination_station_id' : destination_station_id,
        'trip_cancel' : trip_cancel,
        'trip_date': trip_date,
        'trip_length': trip_length,
    })

def check_available_origin(dbname,origin_station_id):
    from models import Model
    model = Model(dbname=dbname)
    check_available = model.select_query(model_name="stations",condition= f'where id ={ origin_station_id} and available_bicycle > 0')
    # print(check_available)
    if len(check_available) > 0:
        return True

def check_available_destination(dbname,destination_station_id):
    from models import Model
    model = Model(dbname=dbname)
    check_available = model.select_query(model_name="stations",condition= f'where id ={ destination_station_id} and available_bicycle > 0')
    # print(check_available)
    if len(check_available) > 0:
        return True


def suggest_origin(dbname,origin_station_id):
    from models import Model
    model = Model(dbname=dbname)
    origin = model.select_query(model_name="stations",condition=f'where id ={origin_station_id}')
    street_name = origin[0]['street_name']
    suggest_origin = model.select_query(model_name="stations",condition= "where street_name ='" +street_name+ "'and available_bicycle > 0")
    # print(suggest_origin[0])
    list_suggusted_origins = []
    for i in suggest_origin:
        list_suggusted_origins.append(i['id'])
    return list_suggusted_origins

def suggest_destination(dbname,destination_station_id):
    from models import Model
    model = Model(dbname=dbname)
    destination = model.select_query(model_name="stations",condition=f'where id ={destination_station_id}')
    street_name = destination[0]['street_name']
    suggest_destination = model.select_query(model_name="stations",condition= "where street_name ='" +street_name+ "'and bicycle_capacity - available_bicycle > 0")
    # print(suggest_destination[0])
    list_suggusted_destination = []
    for i in suggest_destination:
        list_suggusted_destination.append(i['id'])
    return list_suggusted_destination


def create_data_to_trip(dbname,user_id,origin_station_id,origin_acceptance,destination_acceptance,destination_station_id,trip_cancel,trip_date,trip_length):
    from models import Model
    model = Model(dbname=dbname)
    update_data =  model.insert_query(model_name="trips",input_array={
        'user_id': user_id,
        'origin_station_id': origin_station_id,
        'origin_acceptance': origin_acceptance,
        'destination_acceptance': destination_acceptance,
        'destination_station_id': destination_station_id,
        'trip_cancel': trip_cancel,
        'trip_date': trip_date,
        'trip_length': trip_length,
    })

def update_capacities (dbname,origin_station_id,destination_station_id):
    from models import Model
    model = Model(dbname=dbname)
    origin_capacity = model.select_query(model_name="stations",condition= f'where id ={origin_station_id}')
    destination_capacity = model.select_query(model_name= "stations",condition= f'where id ={destination_station_id}')

    update_capacities = model.update_query(model_name="stations", input_array={
        'available_bicycle' : origin_capacity[0]['available_bicycle'] - 1
    },condition= f'where id ={origin_station_id}')

    update_capacities = model.update_query(model_name="stations", input_array={
        'available_bicycle': destination_capacity[0]['available_bicycle'] + 1
    }, condition=f'where id ={destination_station_id}')

