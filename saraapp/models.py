from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.db.models import SET
from django.contrib.auth.models import AnonymousUser

# class Message(models.Model):
#     sender_user = models.ForeignKey(get_user_model(), related_name = 'sender', on_delete= SET(AnonymousUser.id))
#     receiver_user = models.ForeignKey(get_user_model(), related_name= 'recevier', on_delete= SET(AnonymousUser.id))
#     message = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add= True)


# class Room(models.Model):
#     sender_user = models.ForeignKey(get_user_model(), related_name= 'room_sender', on_delete= SET(AnonymousUser.id))
#     receiver_user = models.ForeignKey(get_user_model(), related_name= 'room_receiver', on_delete= SET(AnonymousUser.id))
#     room_name = models.CharField(max_length = 200, unique = True)

#     def __str__(self):
#         return self.room_name





# Create your models here.
# class TextMessage(models.Model):
#     user = models.ForeignKey(get_user_model(), on_delete= models.CASCADE)
#     ffrom = models.IntegerField()
#     to = models.IntegerField()
#     text = models.CharField(max_length= 1000)
#     text_type = models.CharField(max_length= 100, default = 'sms', blank = True)
#     send_date = models.DateField(default = timezone.now())
#     send_time = models.TimeField()
#     date_created = models.DateField(auto_now= True)


# class UserActivity(models.Model):
#     user = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)
#     verb = models.CharField(max_length = 100)
#     target = models.CharField(max_length= 1000)
#     time_stamp = models.DateField(auto_now= True)

