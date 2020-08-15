import random
import uuid

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


def get_t_list():
    return T.select()


def unique_char():
    return uuid.uuid1()


def random_num():
    return random.randint(0, 1000000)


if __name__ == '__main__':
    t_list = get_t_list()
    print(len(t_list))
    share_list = []
    for t in t_list:
        share = Share()
        share.t_id = t.id
        share.unique = unique_char()
        share.desc = '{}abc'.format(random_num())

        share_list.append(share_list)
        Share.save(share)

    Share.insert_many(rows=share_list)
