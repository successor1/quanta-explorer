from ast import Add
from email.headerregistry import Address
from bson.objectid import ObjectId
from pymongo import MongoClient
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from playground.models import Addresses
import datetime
from datetime import datetime as dt

from django.shortcuts import render

from .forms import IndexForm
import json

# meetups = collection.find_one({'_id': ObjectId(id) })
client = MongoClient('127.0.0.1', 27017)

@csrf_exempt
def index(request):
    now = dt.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    db = client['blockchain']

    collection = db['addresses']

    numberwallets = collection.count()

    if request.method == 'POST':
        form = IndexForm(request.POST)
        query = []
        if form.is_valid():
            for key, value in request.POST.items():
                query.append(value)
            return HttpResponseRedirect('/a/' + query[0])
    else:
        form = IndexForm()
    return render(request, 'playground/index.html', {
        'form': form,
        'datetime': dt_string,
        'numberofwallets': numberwallets
        })

def qaddress(request, qaddress):
    db = client['blockchain']

    collection = db['addresses']
    
    data = collection.find_one({'address': qaddress })

    address = data['address']
    balance = data['balance']
    firstSeen = datetime.datetime.fromtimestamp(int(data['firstSeen']))
    lastSeen = datetime.datetime.fromtimestamp(int(data['lastSeen']))
    
    return render(request, 'playground/qaddress.html', {
        'address': address,
        'balance': balance,
        'firstSeen': firstSeen,
        'lastSeen': lastSeen,
    })

def rich_list(request):
    db = client['blockchain']

    collection = db['addresses']

    addresses = collection.find().sort("address", -1).limit(500)
    balances = collection.find().sort("balance", -1).limit(500)

    lists = zip(addresses, balances)
    
    return render(request, 'playground/richlist.html', {
        'lists': lists
    })

def tokens(request):
    db = client['blockchain']

    collection = db['tokens']

    tokens = collection.find().sort("tokenName")

    return render(request, 'playground/tokens.html', {
        'tokens': tokens,
    })

def messages(request):
    db = client['blockchain']

    collection = db['messages']

    messages = collection.find().sort("messageHash")

    return render(request, 'playground/messages.html', {
        'messages': messages,
    })
