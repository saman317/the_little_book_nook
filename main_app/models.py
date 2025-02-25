from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

AGES = (
    ('1-3', '1-3'),
    ('4-6', '4-6'),
    ('7-9', '7-9'),
    ('10-12', '10-12')

)
class Book(models.Model):
    name= models.CharField(default='Book Title')
    image = models.ImageField(upload_to='book/', blank=True, null=True)
    review = models.TextField(default='Review')
    age = models.CharField(
        max_length=5,
        choices=AGES,
        default=AGES[0][0]
    )
    recommend = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_recommend_display(self):
        return "Yes" if self.recommend else "No"

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'book_id': self.id})



class Comment(models.Model):
    recommend = models.BooleanField(default=False)
    review = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"Review: {self.review}"

    def get_recommend_display(self):
        return "Yes" if self.recommend else "No"