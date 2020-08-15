from peewee import Model, PrimaryKeyField, IntegerField, CharField
from playhouse.pool import PooledMySQLDatabase

host = '127.0.0.1'
username = 'root'
password = 'root123'
port = 3306
db = 'my'

pool = PooledMySQLDatabase(db, max_connections=20, stale_timeout=300, user=username, password=password, host=host,
                           port=port)


class BaseModel(Model):
    class Meta:
        database = pool


class T(BaseModel):
    id = PrimaryKeyField()
    a = IntegerField()
    b = IntegerField()


class Share(BaseModel):
    id = PrimaryKeyField()
    t_id = IntegerField()
    unique = CharField()
    desc = CharField()
