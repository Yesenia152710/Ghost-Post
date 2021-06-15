from django.db import models
from django.utils import timezone

# Create your models here.


class Posts(models.Model):

    type_post = models.BooleanField(default=False, null=True)
    text = models.CharField(max_length=150, null=True)
    up = models.IntegerField(default=0)
    down = models.IntegerField(default=0)
    time_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text

    @property
    def total_vote(self):
        return self.up + self.down
