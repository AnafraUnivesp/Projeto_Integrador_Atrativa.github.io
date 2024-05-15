from peewee import Model, CharField, AutoField, DateTimeField
from database.database import db
import datetime

class Camiseta(Model):
    id = AutoField(primary_key=True)
    item = CharField()
    tipo = CharField()
    modelo = CharField()
    cor = CharField()
    tamanho = CharField()
    detalhe = CharField()
    data_registro = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db