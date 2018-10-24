from __future__ import unicode_literals

from django.db import models


class article(models.Model):
    articleid=models.IntegerField(primary_key=True)
    articlecategory=models.CharField(max_length=100)
    articlename=models.CharField(max_length=100)
    articlecontent=models.CharField(max_length=1000000000000)
    writtenby=models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

class reversingarticle(models.Model):
    articleid=models.IntegerField(default=0)
    articlename=models.CharField(max_length=100)

class cryptoarticle(models.Model):
    articleid=models.IntegerField(default=0)
    articlename=models.CharField(max_length=100)

class webarticle(models.Model):
    articleid=models.IntegerField(default=0)
    articlename=models.CharField(max_length=100)

class binaryarticle(models.Model):
    articleid=models.IntegerField(default=0)
    articlename=models.CharField(max_length=100)

class forensicsarticle(models.Model):
    articleid=models.IntegerField(default=0)
    articlename=models.CharField(max_length=100)

class generalarticle(models.Model):
    articleid=models.IntegerField(default=0)
    articlename=models.CharField(max_length=100)



