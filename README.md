﻿# flashcardbackend


This django project needs a utils.py file in the main 'project' folder (the first one)
```python
from pymongo import MongoClient
from django.conf import settings

client = MongoClient('') #<insert mongo connection string in the brackets>
dbname = client['mongodbhackathon']
collection_name = dbname["notes"]
```
