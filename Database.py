import psycopg2
from Question import *

file = open("credentials.txt", "r")
host = file.readline()
database = file.readline()
user = file.readline()
port = file.readline()
password = file.readline()


class DatabaseConnection:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                "dbname= '" + database + "' " +
                "user= '" + user + "' " +
                "host= '" + host + "' " +
                "password= '" + password + "' " +
                "port= '" + port + "'"
            )
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
        except:
            print("Cannot connect to database")

    def create_table(self):
        questions_table_command = "CREATE TABLE IF NOT EXISTS questions(id serial PRIMARY KEY, qname VARCHAR(256) NOT NULL, description VARCHAR(1024))"
        self.cursor.execute(questions_table_command)
        testcases_table_command = "CREATE TABLE IF NOT EXISTS testcases(qname VARCHAR(256) , inputs VARCHAR(256), out VARCHAR(256))"
        self.cursor.execute(testcases_table_command)
        attempts_table_command = "CREATE TABLE IF NOT EXISTS attempts(qname VARCHAR(256), student VARCHAR(256), time TIMESTAMP, successful INTEGER, total INTEGER )"
        self.cursor.execute(attempts_table_command)

    def get_question_name(self):
        self.cursor.execute("SELECT qname from questions")
        return self.cursor.fetchall()


