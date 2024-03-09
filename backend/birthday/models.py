from django.db import models
from django.utils.text import slugify

# Create your models here.
class Birthday(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth_date = models.DateField()
    image = models.ImageField(upload_to='birthday_images/', default='/birthday_images/defImg.webp', blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        # Generate slug from the title if it's not provided
        if not self.slug:
            self.slug = slugify(self.first_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.first_name
