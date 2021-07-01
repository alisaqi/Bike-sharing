from typing import List
from main import connect_to_DB
from psycopg2._psycopg import AsIs
from menu import dbname



class Model:
    cur, conn = connect_to_DB(dbname)

    @classmethod
    def get_attribute(cls,model_name: str, schema: str = 'public', is_view=False):
        if not is_view:
            get_model_attribute_query = "SELECT *  FROM information_schema.columns WHERE table_schema = %s AND table_name   = %s;"
        else:
            get_model_attribute_query = "SELECT *  FROM information_schema.columns WHERE table_schema = %s AND view_name   = %s;"
        cls.cur.execute(get_model_attribute_query, (schema, model_name))
        rows = cls.cur.fetchall()
        attributes = {}
        counter = 1
        for row in rows:
            attributes[row[3]] = counter
            counter = counter + 1
        return attributes

    def __init__(self,dbname) -> None:


    @classmethod
    def select_query(cls, model_name: str = None, schema_name: str = 'public',
                     out_put_array: List[str] = None, condition=None, is_view=False):

        if model_name is not None:
            if not is_view:
                query = 'select * from %s."%s"'
            else:
                query = 'select * from %s.%s '
            if condition is not None:
                query = query + condition
            cls.cur.execute(query, (AsIs(schema_name), AsIs(model_name)))
            rows = cls.cur.fetchall()
            if not is_view:
                attributes = cls.get_attribute(model_name, schema_name)
            else:
                attributes = {}
                count = 1
                for output in out_put_array:
                    attributes[output] = count
                    count += 1
            if out_put_array is not None:
                get_list = {}
                for out_put in out_put_array:
                    try:
                        value = attributes[out_put]
                        get_list[out_put] = value
                    except KeyError:
                        pass
                executed_outputs = []
                for row in rows:
                    executed_output = {}
                    for key, value in get_list.items():
                        executed_output[key] = row[int(value) - 1]
                    executed_outputs.append(executed_output)
                return executed_outputs
            else:
                executed_outputs = []
                for row in rows:
                    executed_output = {}
                    for key, value in attributes.items():
                        executed_output[key] = row[int(value) - 1]
                    executed_outputs.append(executed_output)
                return executed_outputs

    @classmethod
    def insert_query(cls, model_name: str = None, schema_name: str = 'public',
                     input_array: dict = None):
        if model_name is not None:
            query = 'insert into %s."%s" ('
            values = list()
            attributes = cls.get_attribute(model_name=model_name)
            inn = 0
            for key, value in input_array.items():
                if key in attributes.keys():
                    if inn == 0:
                        inn = 1
                    else:
                        query = query + ','
                    query = query + key
                    values.append(value)

            values = tuple(values)
            query = query + ') values' + str(values)
            cls.cur.execute(query, (AsIs(schema_name), AsIs(model_name)))
            cls.conn.commit()

    @classmethod
    def update_query(cls, model_name: str, input_array: dict, schema_name: str = 'public',
                     condition=None):
        if model_name is not None:
            query = 'update %s."%s" set '
            attributes = cls.get_attribute(model_name=model_name)
            inn = 0
            for key, value in input_array.items():
                if key in attributes.keys():
                    if inn == 0:
                        inn = 1
                    else:
                        query = query + ','
                    query = query + key + ' = ' + "'%s'" % (value,)

            if condition is not None:
                query = query + condition
            cls.cur.execute(query, (AsIs(schema_name), AsIs(model_name)))
            cls.conn.commit()

    @classmethod
    def delete_query(cls, model_name: str, condition: str, schema_name: str = 'public'):
        if model_name is not None:
            query = 'delete from %s."%s"' + condition
            cls.cur.execute(query, (AsIs(schema_name), AsIs(model_name)))
            cls.conn.commit()


# rows = Model.select_query(model_name='Customer', out_put_array=['id', 'name', 'f_name'])
# for row in rows:
#     print(row)
# Model.insert_query(model_name='Customer', input_array={'name': "maryam",
#                                                        'f_name': "vaqei",
#                                                        'email': "mwaqei@gmail.com", 'hashd_password': "ppppp",'national_num':1234567})
# Model.update_query(model_name='Customer', input_array={
#     'name': 'Maryam'
# }, condition="where id = 8")
# Model.delete_query(model_name='Customer',condition='where id=8')
def get_filter_list(table_name, filter_column):
    return Model.select_query(model_name=table_name, out_put_array=[filter_column])


def set_filter(objects: List[dict], filter_on: str, wanted_result):
    filtered_objects = []
    for object in objects:
        if object[filter_on] == wanted_result:
            filtered_objects.append(object)
    return filtered_objects
