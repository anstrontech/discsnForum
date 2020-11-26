from django.db import models

# parent model

class User_tab(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=200, default="anonymous")
    contact = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=150)
    create_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


class forum(models.Model):
    userid = models.ForeignKey(User_tab,blank=True, on_delete=models.CASCADE)
    topic = models.CharField(max_length=300)
    description = models.CharField(max_length=1000, blank=True)
    link = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.topic)

# child model
class Discussion(models.Model):
    userid = models.ForeignKey(User_tab,blank=True, on_delete=models.CASCADE)
    forum  = models.ForeignKey(forum, blank=True, on_delete=models.CASCADE)
    discuss = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.forum)