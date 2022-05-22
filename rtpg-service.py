#!/usr/bin/python
import psycopg2
import redis
import json

def read_from_redis():
    r = redis.StrictRedis('localhost', 6379, charset='utf-8', decode_responses=True)
    redis_value = r.blpop("channel:jawaker")
    dict_value = json.loads(redis_value[1])
    return(str(dict_value['username']))


def insert_username(username):
    query = "INSERT INTO users (username) VALUES (%s);"
    conn = None
    try:
        # connect to the database
        conn = psycopg2.connect(
            host="localhost",
            database="jawaker",
            user="jawaker",
            password="123",
            connect_timeout=10)
        #create a curser
        cur = conn.cursor()
        # execute the insert statement
        cur.execute(query, (username,))
        #commit changes to the database
        conn.commit()
        print('One value written to Database.')
        #close connection with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        print('Database connection closed.')
    finally:
        if conn is not None:
            conn.close()
            
    return 0
if __name__ == '__main__':
    while True:
        username = read_from_redis()
        insert_username(username)
