from django.db import models

"""
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
"""
class TruckModel(models.Model):
    name = models.CharField(max_length=50,null=True, blank=True)
    max_weight = models.FloatField()

    def __str__(self):
        return self.name

class Truck(models.Model):
    name = models.CharField(max_length=50,null=True, blank=True)
    model = models.ForeignKey('TruckModel')
    curr_weight = models.FloatField()
    garage_number = models.CharField(max_length=50)

    def __str__(self):
        return self.name
