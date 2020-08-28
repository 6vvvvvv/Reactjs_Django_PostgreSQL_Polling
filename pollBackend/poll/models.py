from django.db import models


class Polling(models.Model):
    id = models.IntegerField(
        primary_key=True, unique=True)
    option = models.CharField(max_length=30, default="")
    vote = models.IntegerField()
    rate = models.FloatField()

    def __str__(self):
        return self.option

    @classmethod
    def create_polling(cls, id, option, vote, rate):
        alternative = cls(
            id=id, option=option, vote=vote, rate=rate)
        return alternative
