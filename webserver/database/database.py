<<<<<<< HEAD
from peewee import  SqliteDatabase


db = SqliteDatabase('estoque.db')


=======
import os
from peewee import PostgresqlDatabase
from dotenv import load_dotenv

load_dotenv()

db = PostgresqlDatabase(os.getenv('DATABASE_URI', ''))
>>>>>>> origin
