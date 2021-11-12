from django.db import models

# Second import


# Create your models here.
SEMESTER_CHOICES = (
    ("remote", "remote"),
    ("full time", "full time"))

TIME = (
    ("1 year", "1 year"),
    ("2 years", "2 years"),
    ("3 years", "3 years"),
    ("4 years", "4 years"))

ANOTHER = (("Full stack", "Full stack"),
            ("Frontend", "Frontend"),
            ("Backend", "Backend"),
            ("Data Scientist", "Data Scientist"),
            ("Data Analyst", "Data Analyst"))


class Job(models.Model):
    title = models.CharField(max_length=200, blank=True)
    company = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=200, blank=True)
    type = models.CharField(
        max_length = 20,
        choices = SEMESTER_CHOICES,
        default = False
        )
    experience = models.CharField(
        max_length = 20,
        choices = TIME,
        default = False
        )
    profession = models.CharField(
        max_length = 20,
        choices = ANOTHER,
        default = False
        )
# Second class for application

class AppList(models.Model):
   name = models.CharField(max_length=100)
   email = models.CharField(max_length=100)
   birth_date = models.DateField(null=False)
   qualification = models.CharField(max_length=100)