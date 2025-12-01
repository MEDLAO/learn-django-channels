from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from chat.models import Message


@login_required
def chat_view(request):
    room_name = "room2"
    messages = Message.objects.filter(room_name=room_name).order_by("timestamp")[:50]

    return render(request, "chat.html", {"messages": messages, "room_name": room_name, })
