from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import truncatechars  # or truncatewords

# Create your models here.

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural='categories'

    def __str__(self):
        return self.name


class FlashCard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    question = models.TextField()
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    @property
    def title(self):
        return truncatechars(self.question, 10)

    def __str__(self):
        return f'{self.question[:10]}...'
