import psycopg2
import main


def create_tables(name):
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        create table stations(
        id SERIAL PRIMARY KEY ,
        name varchar(255),
        address_id INTEGER,
        street_name varchar(255),
        bicycle_capacity INTEGER,
        available_bicycle INTEGER,
        park_capacity INTEGER)
        
        """,
        """
                create table users(
                id SERIAL PRIMARY KEY,
                code_melli INTEGER,
                name varchar(255),
                last_name varchar(255),
                birthdate DATE,
                register_date DATE NOT NULL DEFAULT CURRENT_DATE,
                gender BOOL)
    
                """
        ,
        """
        
        create table trips(
        id SERIAL PRIMARY KEY ,
        user_id INTEGER NOT NULL,
        origin_station_id INTEGER NOT NULL,
        origin_acceptance bool,
        destination_acceptance bool,
        destination_station_id INTEGER NOT NULL,
        trip_cancel bool,
        trip_date DATE,
        trip_length INTEGER,
        FOREIGN KEY (origin_station_id)
                    REFERENCES stations (id)
                    ON UPDATE CASCADE ON DELETE CASCADE,
        FOREIGN KEY (destination_station_id)
                    REFERENCES stations (id)
                    ON UPDATE CASCADE ON DELETE CASCADE,
        FOREIGN KEY (user_id)
                    REFERENCES users (id)
                    ON UPDATE CASCADE ON DELETE CASCADE            
        )
        
        """)
    cur,conn = main.connect_to_DB(name = name)
    try:
        # read the connection parameters
        # params = config()
        # connect to the PostgreSQL server
        # conn = psycopg2.connect(**params)
        # cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    print("tables are created")
