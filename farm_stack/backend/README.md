mongodb:
username: mongoDbUser
password: joHgyfnZPIVSUoNe

```python
client = pymongo.MongoClient("mongodb+srv://mongoDbUser:<password>@cluster0.kgulu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test

# Replace <password> with the password for the mongoDbUser user. Replace myFirstDatabase with the name of the database that connections will use by default. Ensure any option params are URL encoded.
```

[current timestamp](https://youtu.be/OzUzrs8uJl8?t=2433)
