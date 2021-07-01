

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


