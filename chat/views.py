from django.shortcuts import render

from chat.models import Message
from chat.models import Chat

# Create your views here.

def index(request):
    if request.method == 'POST':
        print("received data " + request.POST['textmessage'])
        myChat = Chat.objects.get(id=1)
        Message.objects.create(text = request.POST['textmessage'], chat = myChat, author= request.user, receiver= request.user)
    return render(request, 'chat/index.html', {'username': 'Alex'})