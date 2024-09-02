from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15)
    course = models.CharField(max_length=50)
    semester = models.CharField(max_length=10)
    batch = models.CharField(max_length=50)
    roll_number = models.CharField(max_length=20)
    status = models.CharField(max_length=10, default='Active')
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.user.username

class Resource(models.Model):
    title = models.CharField(max_length=200)
    resource_type = models.CharField(max_length=50)  # e.g., PDF, Video, Link
    file = models.FileField(upload_to='resources/', blank=True, null=True)
    url = models.URLField(blank=True, null=True)

class LearningPath(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    resources = models.ManyToManyField(Resource)
    total_time = models.IntegerField()  # in minutes

class Progress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    learning_path = models.ForeignKey(LearningPath, on_delete=models.CASCADE)
    completed_time = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)

