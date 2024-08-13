from django.shortcuts import render

# Create your views here.

rooms = [
    {'id': 1, 'name': 'Djangooooooo'},
    {'id': 2, 'name': 'Djangooooooo with chains'},
    {'id': 3, 'name': 'Djangooooooo unchained'}
]

def home(request):
    context =  {'rooms': rooms}
    return render(request, 'home.html',context)

def room(request):
    return render(request, 'room.html')
