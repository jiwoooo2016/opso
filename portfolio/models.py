from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def average_score(self):
        ratings = self.ratings.all()
        if ratings.exists():
            return sum(r.score for r in ratings) / ratings.count()
        return 0

class Rating(models.Model):
    project = models.ForeignKey(Project, related_name='ratings', on_delete=models.CASCADE)
    score = models.IntegerField()
