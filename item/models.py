from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class ItemCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description=models.CharField(max_length=50,default='No description available')

    class Meta:
        ordering=('name',)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE, related_name='items')
    provider_name = models.CharField(max_length=255, blank=True)  # hospital, lab, pharmacy, etc.
    location = models.CharField(max_length=255, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    available_online = models.BooleanField(default=False)
    is_sold = models.BooleanField(default=False)
    # image = models.ImageField(upload_to='items_images', null=True, blank=True)
    image = CloudinaryField('image', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items', null=True)

    # created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items')

    def __str__(self):
        return f"{self.name} ({self.category.name})"



class Rating(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.PositiveSmallIntegerField()  # 1 to 5
    review = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('item', 'user')  # one rating per user per item

    def __str__(self):
        return f"{self.score}⭐ by {self.user.username} for {self.item.name}"


# Create your models here.

