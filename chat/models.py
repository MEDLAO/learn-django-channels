from django.db import models
from django.conf import settings


class Message(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room_name = models.CharField(max_length=255)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    #def __str__(self):
    #    return f"{self.user.username}: {self.content[:20]}"
    def __str__(self):
        return f"Message from user {self.user_id}"


class DirectMessage(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sent_direct_messages")
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="received_direct_messages")
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["timestamp"]

    #def __str__(self):
    #       return f"{self.sender.username} -> {self.receiver.username}: {self.content[:20]}"

    def __str__(self):
        return f"DM {self.id} ({self.sender_id} -> {self.receiver_id})"

