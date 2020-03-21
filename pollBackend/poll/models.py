from django.db import models



class Pollingoption(models.Model):
    option = models.CharField(max_length=100)
    vote = models.IntegerField(default="0")


class Pollingtitle(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        """A string representation of the model."""
        return self.title
