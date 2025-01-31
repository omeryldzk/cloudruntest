from google.cloud import storage
import random
def add(a, b):
    return a + b

def create_bucket_class_location(bucket_name):
    """
    Create a new bucket in the US region with the coldline storage
    class
    """
    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)
    bucket.storage_class = "COLDLINE"
    new_bucket = storage_client.create_bucket(bucket, location="us")

    print(
        "Created bucket {} in {} with storage class {}".format(
            new_bucket.name, new_bucket.location, new_bucket.storage_class
        )
    )
    return new_bucket

# Generate two random integers
a = random.randint(1, 100)
b = random.randint(1, 100)
x = add(a,b)
create_bucket_class_location("bucket{}-demo".format(x))