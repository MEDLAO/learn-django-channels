from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from chat.models import Message


@login_required
def chat_view(request, room_name):
    messages = Message.objects.filter(room_name=room_name).order_by("timestamp")[:50]
    return render(request, "chat.html", {"messages": messages, "room_name": room_name, })


def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # create the new user
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(request, "signup.html", {"form": form})
