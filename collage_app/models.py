from django.db import models



class Serie(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    slug = models.SlugField(max_length=100, blank=False, unique=True)
    image = models.ImageField(upload_to='uploads/')
    date = models.DateField(auto_now=True)
    active_choices = [
    ("ACTIVE", "Active"),
    ("SOLD", "Sold"),
]
    choices = models.CharField(max_length=20, choices=active_choices, blank=False)

    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return f'/serie/{self.slug}/'

    def get_image(self):
            return 'http://192.168.112.97:8000' + self.image.url


class Token(models.Model):
    serie = models.ForeignKey(Serie, related_name='tokens', on_delete=models.CASCADE)
    number = models.CharField(max_length=200)
    author = models.CharField(max_length=300)
    title = models.TextField()
    image = models.ImageField(upload_to='uploads/')
    date = models.DateField(auto_now=True)

    def get_image(self):
            return 'http://192.168.112.97:8000' + self.image.url