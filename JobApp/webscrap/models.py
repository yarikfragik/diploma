from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Tags(models.Model):
    """
        Model for storing all the requested Tags from the user
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    skill = models.CharField(max_length=100, null=False, blank=False)
    date_of_req = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.skill

    class Meta:
        ordering = ["date_of_req"]


class jobDetails(models.Model):
    company_name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    link = models.URLField(max_length=5000)
    description = models.TextField(null=True, blank=True)
    tag = models.ForeignKey(Tags, null=False, blank=False, on_delete=models.CASCADE)  # foreign key
    date_of_entry = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Personalize(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    skill = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.skill

    def get_personalised_data(self):
        details = jobDetails.objects.filter(tag__skill=self.skill).all()
        return details


class Contact(models.Model):
    email = models.CharField(max_length=100, default="")
    username = models.CharField(max_length=100, default="")
    query = models.CharField(max_length=1000, default="")

    def __str__(self):
        return self.username
