"""
--> nothing, <-- greeting random name
User types in Name, getting greet
"""
import faker

for i in range(100):
    print('hello {}'.format(faker.Factory.create().name()))