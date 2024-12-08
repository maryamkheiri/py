from mysql.connector import connection
from mysql.connector import Error
import logging
import time

# cnn=connection.MySQLConnection(
#     host="127.0.0.1",
#     user="root",
#     password="1234",
#     database="mydb"
# )
# if cnn.is_connected():
#     print("connected")
#Set Up Logger:
logger=logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter=logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

#Log To Console
handler=logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)

#Also Log To File
file_handler=logging.FileHandler("cpy-errors.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def connect_to_mysql(config,attemps=3,delay=2):
    attemp=1
    # Implement a reconnection routine
    while attemp<attemps+1:
        try:
            return connection.MySQLConnection(**config)
        except (Error,IOError) as err:
            if (attemp is attemps):
                 # Attempts to reconnect failed; returning None
                 logger.info(
                     "failed to connect,exsiting without a connection:%s",err)
                 return None
            logger.info(
                "connection failed: %s.retrying(%d,%d)...",
                err,
                attemp,
                attemps-1
            )
            time.sleep(delay**attemp)
            attemp+=1
    return None

                 

config = {
  'user': 'root',
  'password': '1234',
  'host': '127.0.0.1',
  'database': 'mydb',
  'raise_on_warnings': True
}

cnn=connect_to_mysql(config)
cursor1=cnn.cursor()
query="CREATE TABLE IF NOT EXISTS transaction (tansaction_id INT PRIMARY KEY AUTO_INCREMENT ,amount DECIMAL(5,2))"
cursor1.execute(query)
cnn.commit()
query="INSERT INTO transaction(tansaction_id,amount)VALUES(%s)"
values=[(4.99,),(5.77,),(6.90,),(1.00,)]
cursor1.executemany(query,values)
cnn.commit()
query="SELECT * FROM transaction WHERE 1"
cursor1.execute(query)
for i in cursor1:
    print(i)

