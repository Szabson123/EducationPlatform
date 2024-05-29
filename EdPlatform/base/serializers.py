from rest_framework import serializers
from .models import *


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        

class DescriptionToArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = DescriptionToArticle
        fields = '__all__'


class ImageToArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageToArticle
        fields = '__all__'


class CodeToArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeToArticle
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class PresetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preset
        fields = '__all__'