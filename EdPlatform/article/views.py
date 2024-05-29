from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from base.serializers import *
from base.models import *

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response



class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
    @action(detail=True, methods=['PATCH'])
    def put_online_or_offline_article(self, request, pk=None):
        article = get_object_or_404(Article, pk=pk)
        
        if article.draft:
            article.draft = False
            article.upload_date = timezone.now()
            message = "You've put the Article online"
            
        else:
            article.draft = True
            message = "You've put the Article offline"
        
        article.save()
        serializer = ArticleSerializer(article, many=False)
        return Response({"message": message, 'result': serializer.data,}, status=status.HTTP_200_OK)
        
        
class DescriptionToArticleViewSet(viewsets.ModelViewSet):
    queryset = DescriptionToArticle.objects.all()
    serializer_class = DescriptionToArticleSerializer

    @action(detail=True, methods=['POST'])
    def create_description(self, request, pk=None):
        article = get_object_or_404(Article, pk=pk)
        description_data = request.data.get('description', '')
        description_element = DescriptionToArticle.objects.create(article=article, description = description_data)
        serializer = DescriptionToArticleSerializer(description_element, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class ImageToArticleViewSet(viewsets.ModelViewSet):
    queryset = ImageToArticle.objects.all()
    serializer_class = ImageToArticleSerializer
    
    @action(detail=True, methods=['POST'])
    def create_image(self, request, pk=None):
        article = get_object_or_404(Article, pk=pk)
        image_data = request.FILES.get('image')
        image_element = ImageToArticle.objects.create(article=article, image=image_data)
        serializer = ImageToArticleSerializer(image_element, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CodeToArticleViewSet(viewsets.ModelViewSet):
    queryset = CodeToArticle.objects.all()
    serializer_class = CodeToArticleSerializer

    @action(detail=True, methods=['POST'])
    def create_code(self, request, pk=None):
        article = get_object_or_404(Article, pk=pk)
        code_data = request.data.get('code', '')
        code_element = CodeToArticle.objects.create(article=article, code=code_data)
        serializer = CodeToArticleSerializer(code_element, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
