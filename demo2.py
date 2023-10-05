from rq import Queue
from redis import Redis

from tasks import sample, add

# Connect to the Redis server
redis_conn = Redis(host='localhost', port=6379)

# Create a queue
queue = Queue(connection=redis_conn)
