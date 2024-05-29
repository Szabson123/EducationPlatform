from django.contrib import admin
from base.models import *

admin.site.register(Article)
admin.site.register(DescriptionToArticle)
admin.site.register(ImageToArticle)
admin.site.register(CodeToArticle)
admin.site.register(Comment)
admin.site.register(Preset)
