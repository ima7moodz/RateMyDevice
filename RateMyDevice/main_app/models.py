from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
CATEGORY = (
    ('P', 'Smart Phone'),
    ('L', 'Laptops'),
    ('M', 'Machines'),
    ('T', 'Tablet'),
    ('O','Others')
)

class Device(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=1, choices=CATEGORY, default=[0][0])
    description = models.TextField(max_length=250)
    rate = models.DecimalField(max_digits=8, decimal_places=0, default=0)
    warrenty_expration_Date = models.DateField()
    opinion = models.TextField(max_length=250)
    likes = models.ManyToManyField(User, related_name='liked_devices', blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('device-detail', kwargs={'device_id': self.id})

    def total_likes(self):
        return self.likes.count()


class Reviews(models.Model):
    comments =models.TextField(max_length=250)
    devices = models.ForeignKey(Device, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} on {self.comments}"
    class Meta:
        ordering = ['-id']

class Chat(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_chats")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_chats")
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chat between {self.sender.username} and {self.receiver.username}"
    
class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name="messages")
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.username}: {self.content}"
