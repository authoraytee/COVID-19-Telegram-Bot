import mysql.connector
from mysql.connector import Error

def connect(question_id):

    try:
        conn = mysql.connector.connect(host='localhost',database='covid_bot',user='root',password='password1122')
        if conn.is_connected():
            print('Connected to MySQL database')
        

        text = ['']
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
                  



