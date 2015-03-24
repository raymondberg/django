from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Neighborhood(models.Model):
    name = models.CharField(max_length=256)
    zip_code = models.CharField(max_length=10)
#   neighbors = models.ManyToManyField(Neighborhood)

    def __unicode__(self):
        return self.name

# Create your models here.
class Animal(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField()
    phone = models.CharField(max_length=14)
    neighborhood = models.ForeignKey(Neighborhood, blank=True,null=True)
    ratings = models.ManyToManyField('self', through="AnimalRating", related_name="ratings+", symmetrical=False)

    def __unicode__(self):
        return self.first_name

    def rate(self, ratee, liking=5, tagalong=1):
        ar = AnimalRating(rater=self, ratee=ratee, liking=liking, tagalong=tagalong)
        ar.save()

    def clear_rating(self, ratee):
        ratings = AnimalRating.objects.filter(ratee=ratee)
        for rating in ratings:
            rating.delete()

    def get_ratings(self):
        return AnimalRating.objects.filter(rater=self)

class AnimalRating(models.Model):
    rater = models.ForeignKey(Animal, related_name="by_animal")
    ratee = models.ForeignKey(Animal, related_name="of_animal")
    liking = models.IntegerField(
            validators=(
                MaxValueValidator(9),
                MinValueValidator(0)
            )
    )
    tagalong = models.IntegerField()

    def __unicode__(self):
        return "%s -> %s" % (self.rater, self.ratee)
