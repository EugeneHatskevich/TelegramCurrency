from peewee import *
import datetime


db_name = 'currency.sqlite'
db = SqliteDatabase(db_name)


class Currency(Model):
    id = PrimaryKeyField()
    name = CharField()
    count = IntegerField()
    code = CharField()
    value = DecimalField()

    created_at = DateTimeField(default=datetime.datetime.now())
    updated_at = DateTimeField(default=datetime.datetime.now())

    class Meta:
        database = db
