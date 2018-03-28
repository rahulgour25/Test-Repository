#!C:\Python34
import psycopg2
from config import config
#changes1
def getserverdetails(serverid):	
    """ Connect to the PostgreSQL Rahul database server """
    conn = None

    try:
        # read connection parameters
        params = config()			
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        # create a cursor
        cur = conn.cursor()
        # execute a statement
        cur.execute("SELECT * from MST_SERVER_DETAILS where server_id = %s;",[serverid])
        # display the PostgreSQL database server version
        db_records = cur.fetchall()
        #print("The number of parts: ", cur.rowcount)
        for row in db_records:
          #print(row)
          # close the communication with the PostgreSQL
         cur.close()
        return row
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)