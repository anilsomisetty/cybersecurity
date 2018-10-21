from __future__ import unicode_literals

from django.db import models

class question(models.Model):
    questionid=models.IntegerField(default=0)
    question=models.CharField(max_length=1000)
    hints=models.CharField(max_length=1000)
    answer=models.CharField(max_length=100,null=True,default="n")
class article(models.Model):
    articleid=models.IntegerField(default=0)
    articlename=models.CharField(max_length=100)