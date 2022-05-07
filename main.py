import redis
import os

redis_host = os.getenv('REDIS_HOST', 'redis')
redis_port = os.getenv('REDIS_PORT', 6379)
redis_password = os.getenv('REDIS_PASSWORD', '')

def ping_redis():
    try:
        r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

        print(r.ping()) # You should see "True" if it worked

    except Exception as e:
        print(e)

def lambda_handler(event, context):
    ping_redis()

if __name__ == '__main__':
    ping_redis()
