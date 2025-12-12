from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from chat.models import Message, DirectMessage


User = get_user_model()


@login_required
def chat_view(request, room_name):
    messages = Message.objects.filter(room_name=room_name).order_by("timestamp")[:50]
    return render(request, "chat.html", {"messages": messages, "room_name": room_name, })


@login_required
def dm_view(request, username):
    # user I want to chat with
    other_user = get_object_or_404(User, username=username)
    # the logged-in user
    current_user = request.user
    # get the full conversation
    messages = DirectMessage.objects.filter(
        sender__in=[current_user, other_user],
        receiver__in=[current_user, other_user],
    )

    return render(request, "dm.html", {"other_user": other_user, "messages": messages, })


def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # create the new user
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(request, "signup.html", {"form": form})
