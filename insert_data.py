from models import Model

def create_user(national_number,name,lastname,birth_date,gender):
    user = Model.insert_query(model_name='users',input_array={
        'code_melli':national_number,
        'name':name,
        'last_name':lastname,
        'birthdate':birth_date,
        'gender':gender,
    })


