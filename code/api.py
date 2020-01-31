import json
import pyrebase
config = {
              "apiKey": "apiKey",
              "authDomain":"geographicindicationspl.firebaseapp.com" ,
              "databaseURL": "https://geographicindicationspl.firebaseio.com/",
              "storageBucket":"geographicindicationspl.appspot.com/",
              #"serviceAccount": "path/to/serviceAccountCredentials.json"
            }
firebase = pyrebase.initialize_app(config)
db = firebase.database()
users = db.child("Questions/CRICKET").get()
dlink=users.val()
for i in dlink:
    print(type(dlink[i]))
