from django.db import models

# Create your models here.


class User_Action(models.Model):
    role = models.CharField(max_length=255,blank=True)
   

# table content use name instead of contactobject 1 2 ...
    def __str__(self):
        return self.name
class Score(models.Model):
    user_score = models.CharField(max_length=255,blank=True,default=0)
    bot_score = models.CharField(max_length=255,blank=True,default=0)
    tie = models.CharField(max_length=255,blank=True,default=0)

class User_input(models.Model):
    name = models.CharField(max_length=255,blank=True)
    # email = models.CharField(max_length=122)
    # phone = models.CharField(max_length=12)
    # desc = models.TextField()
    # date = models.DateField()

# table content use name instead of contactobject 1 2 ...
    def __str__(self):
        return self.name
