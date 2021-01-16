import mysql.connector
from mysql.connector import Error

def connect():
    conn = mysql.connector.connect(host='localhost',database='covid_bot',user='root',password='password1122')
    if conn.is_connected():
        print('Connected to MySQL database')
    else: 
        print('Connection to database failed, try later')
    cursor = conn.cursor()

    return conn
        

def get_questions():
    try:
        conn = connect()

        text = []
        cursor = conn.cursor()
        
        for i in range(15):
            cursor.execute("SELECT Question FROM qanda WHERE Id={};".format(i+1))
            row = cursor.fetchone()
            text.append('/FAQ_{} '.format(i+1) + row[0])

            text.append('')

        text = '\n'.join(text)

        return text  

    except Error as e:
        print(e)

    finally:
        conn.close()


def get_answer(question_id):

    try:
        conn = connect()

        text = []
        cursor = conn.cursor()
        cursor.execute("SELECT Question FROM qanda WHERE Id={};".format(question_id))
        row = cursor.fetchone()
        text.append('----- ' +  row[0] + '-----')

        text.append('')

        cursor.execute("SELECT Answer FROM qanda WHERE Id={};".format(question_id))
        row = cursor.fetchone()
        text.append(row[0])


        text = '\n'.join(text)


        return text  

    except Error as e:
        print(e)

    finally:
        conn.close()

