from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
# Create your models here.
class Book(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    content = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    cover = models.ImageField(upload_to='book_covers/', blank=True)

    def __str__(self):
        return f"{self.title} - {self.author}"

    def get_absolute_url(self):
        return reverse('book_detail',args=[self.id])

class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE,related_name="comments")
    content = models.TextField()
    datetime_create = models.DateTimeField(auto_now_add=True)
    recommend = models.BooleanField(default=False)
    is_shown = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user} - {self.book} : {self.content}"
