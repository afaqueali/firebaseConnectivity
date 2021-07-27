from django.shortcuts import render
from django.http import HttpResponse
import pyrebase

config={
    "apiKey": "AIzaSyBkQGUS-XqXbxx_x-8ykeuKJj6GZB0k70s",
    "authDomain": "test-ea375.firebaseapp.com",
    "databaseURL": "https://test-ea375-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "test-ea375",
    "storageBucket": "test-ea375.appspot.com",
    "messagingSenderId": "454145256221",
    "appId": "1:454145256221:web:fe4557142ec323112f4ff4",
    "measurementId": "G-E99100VVNP"
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()

#def calculate():
 #   x = 1
  #  y = 2
   # return x

def index(request):
    #x = calculate()
    channel_name = database.child('Data').child('Name').get().val()
    channel_type = database.child('Data').child('Type').get().val()
    channel_subs = database.child('Data').child('Subscribers').get().val()
    
    return render(request, 'index.html',{
        "channel_name":channel_name,
        "channel_type":channel_type,
        "channel_subs":channel_subs,
    }) 

#    return render(request, 'hello.html', {'name': 'Afaque'}) 

# Create your views here.
