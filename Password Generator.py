#Don't  you dare to Judge me!This one is my first project to check how could i upload
import random
import string

length =12

characters =string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for i in range(length))

print("Your Password:",password)
