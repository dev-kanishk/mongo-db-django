# django-mongodb-mysql

IMP Link - https://fernandorodrigues.pro/creating-a-rest-apiwebservice-with-django-rest-framework-and-mongo-mongoengine-using-python-3/

Create a Database With Name `testdb` in MongoDB

For Now we are uing sqlite3 for authentication

in virtualenv

`pip install - requirements.txt`


`http://localhost:8000/chatbox/`

```
{
"title": "Chatbox1"
}
```

Refresh

`http://localhost:8000/chatbox/<chatbox_ID_here>/`

```
{
"title": "Chatbox11"
}
```

Refresh

`http://localhost:8000/chatbox/<chatbox_ID_here>/component-add/`
```
{
"name":"Component1",
"questions":["Question1", "Question2"],
"response_type":"DAT"
}
```

Try to implement this `http://localhost:8000/chatbox/<chatbox_id>/component/<component_id>/`

Where we want to update and Delete ListField of Embedded Document. Lets say we want to update data of component which we have added using this `http://localhost:8000/chatbox/<chatbox_ID_here>/component-add/`

