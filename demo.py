import time

from rq import Queue
from redis import Redis
from rq.job import Job

from tasks import sample, print_name

# Connect to the Redis server
redis_conn = Redis(host='localhost', port=6379)

# Create a queue
queue = Queue(connection=redis_conn)


# Enqueue tasks with arguments
job1 = queue.enqueue(sample)
job2 = queue.enqueue(print_name, "Alice")
job3 = queue.enqueue(print_name, "Bob")
job4 = queue.enqueue(print_name, "Charlie")

# Demonstrate job IDs
print(f"Job1 ID: {job1.id}")
print(f"Job2 ID: {job2.id}")
print(f"Job3 ID: {job3.id}")
print(f"Job4 ID: {job4.id}")

# Set a timeout for long polling (in seconds)
timeout = 20
start_time = time.time()

# Long polling loop
while not all(job.is_finished for job in [job1, job2, job3]):
    # Sleep for a short time to avoid high CPU usage
    time.sleep(0.5)

    # Check if the timeout has been reached
    if time.time() - start_time > timeout:
        print("Results not available within the timeout.")
        break

# Fetch job results and display them
for job in [job1, job2, job3]:
    job = Job.fetch(job.id, connection=redis_conn)
    print(f"Job ID: {job.id}, Status: {job.get_status()}, Result: {job.result}")


# Continue with the main function without waiting for the task to finish
print("The main function does not wait for the background task to complete.")


