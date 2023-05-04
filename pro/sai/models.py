
from django.db import models
from django.db.models import ForeignKey


from django.contrib.auth.models import User


class CUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pattern = models.CharField(max_length=64)

    def __str__(self):
        return self.user.username

    # def update_user_id(cls, username):
    #     user_instance = User.objects.get(username=username)
    #     custom_user_instance = cls.objects.get(user=user_instance)
    #     custom_user_instance.user_id = user_instance.pk
    #     custom_user_instance.save()



    

