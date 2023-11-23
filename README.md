# flashcardbackend


This django project needs a utils.py file in the main 'project' folder (the first one)
```python
from pymongo import MongoClient
from django.conf import settings

client = MongoClient('') #<insert mongo connection string in the brackets>
dbname = client['mongodbhackathon']
collection_name = dbname["notes"]
```
# What needs to be added
 ## AI
 ### Generate Flash Card
 This is a will be a get recieving a topic and returns the questions

 ## Database
 ### Store Flashcard
 POST 
 this will recieve a list of objects and we send it to DB

 ### Delete Flashcard
 Delete
 this will take a question object and it from the user's cards
 but i don't know how are we going to sort and organize all the flashcard id 

 ## Quiz
GET
recieve a list of flashcards associated with a user 