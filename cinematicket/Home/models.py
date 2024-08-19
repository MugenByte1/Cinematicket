from django.db import models

class Movie(models.Model):
    CATEGORY_CHOICES = [
        ('Iranian', 'Iranian Film'),
        ('Comedy', 'Comedy Theater'),
        ('Theater', 'Theater'),
        ('Children', 'Children and Teenagers'),
        ('Foreign', 'Foreign Film'),
        ('Art', 'Art and Experience'),
    ]
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField()
    director = models.CharField(max_length=40, default='Unknon')
    rating = models.FloatField(default=5.0)

    def __str__(self):
        return self.title
