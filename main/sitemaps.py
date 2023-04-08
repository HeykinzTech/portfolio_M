from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from myapp.models import Post,Category

class CategorySitemap(Sitemap):
    def items(self,request):
        return Category.objects.all()
    
class PostSitemap(Sitemap):
    def items(self,request):
        return Post.objects.filter(status= Post.ACTIVE)
    def lastmod(self, obj):
        return obj.created_at
