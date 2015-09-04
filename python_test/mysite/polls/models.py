

# Create your models here.
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200, null=True)
    question_text1 = models.CharField(max_length=200,null=True)
    question_text2 = models.CharField(max_length=200,null=True)
    question_text3 = models.CharField(max_length=200,null=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Key(models.Model):
    sport =models.CharField(max_length=200)
    key_test = models.OneToOneField(Question)
