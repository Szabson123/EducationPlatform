from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    upload_date = models.DateTimeField(auto_now_add=True)
    draft = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class DataToArticle(models.Model):
    ARTICLE_ELEMENT_TYPES = (
        ('description', 'Description'),
        ('image', 'Image'),
        ('code', 'Code')
    )
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='elements')
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='article_image/', blank=True, null=True)
    code = models.TextField(blank=True, null=True)
    element_type = models.CharField(choices=ARTICLE_ELEMENT_TYPES, max_length=20)
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    text = models.TextField()
    upload_date = models.DateTimeField()

    def __str__(self):
        return f'Comment on {self.article.title}'
    

class Preset(models.Model):
    title = models.CharField(max_length=255)
    code = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='preset_image/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title