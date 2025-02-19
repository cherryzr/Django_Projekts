from django.db import models

# Create your models here.

# In our poll app, we’ll create two models: Question and Choice.
# A Question has a question and a publication date.
# A Choice has two fields: the text of the choice and a vote tally.
# Each Choice is associated with a Question.

# each class, table and choice becomes a tale in the db
# each variable inside the class becomes the column in the table


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    # ForeignKey(Question, on_delete=models.CASCADE) = Links Choice to Question.
    # If a Question is deleted, all its Choice options get deleted too.
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


# Basically, this code is making a simple poll system where:

# Question stores a question and when it was posted.
# Choice stores possible answers and how many votes they got.
# Every Choice is linked to a Question with a foregin key.
