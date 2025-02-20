from django.db import models
from django.utils import timezone
import datetime

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

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = "pub_date"
    was_published_recently.boolean = True
    was_published_recently.short_description = "Published recently?"


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


# Basically, this code is making a simple poll system where:

# Question stores a question and when it was posted.
# Choice stores possible answers and how many votes they got.
# Every Choice is linked to a Question with a foregin key.


"""
In Django (and programming in general), a model is just a blueprint for storing data in a database.

Think of it like this:

You have a real-world thing you want to keep track of, like a poll question and its choices.
Instead of working directly with the database (which is messy), you define a model in Python to tell Django:
What data to store (text, numbers, dates, etc.).
How different data pieces relate (like Choices belonging to a Question).
Why is "model" used so much?
Because Django follows the "Model-View-Controller" (MVC) pattern, where:

Model = Handles the data (database structure).
View = Handles what users see.
Controller = Handles the logic (Django combines this into "views").
In simple terms, models = database tables, but in Python form. Instead of writing raw SQL, you describe your data using models, and Django takes care of the rest.


That small bit of model code gives Django a lot of information. With it, Django is able to:

Create a database schema (CREATE TABLE statements) for this app.

Create a Python database-access API for accessing Question and Choice objects.
"""
