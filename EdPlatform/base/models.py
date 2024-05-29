from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    upload_date = models.DateTimeField(auto_now_add=True)
    draft = models.BooleanField(default=True)

    def __str__(self):
        return self.title
        

class DescriptionToArticle(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='desc_elements')
    description = models.TextField(blank=True, null=True)
    
    def __str__(self) -> str:
        return f'Content for {self.article.title}'
    

class ImageToArticle(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='img_elements')
    image = models.ImageField(upload_to='article_image/', blank=True, null=True)
    
    def __str__(self) -> str:
        return f'Image for {self.article.title}'
    

class CodeToArticle(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='code_elements')
    description = models.TextField(blank=True, null=True)
    
    def __str__(self) -> str:
        return f'Code for {self.article.title}'
    

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment on {self.article.title}'
    

class Preset(models.Model):
    title = models.CharField(max_length=255)
    code = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='preset_image/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title