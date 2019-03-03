import redis


# redis_client = redis.Redis(host='127.0.0.1', port=6379, db=0, decode_responses=True)
# name = redis_client.get("name")
# print(name)

redis_pool = redis.ConnectionPool(host="127.0.0.1", port=6379, decode_responses=True)
redis_pool_client = redis.Redis(connection_pool=redis_pool, db=0)
name = redis_pool_client.get("name")

print(name)
