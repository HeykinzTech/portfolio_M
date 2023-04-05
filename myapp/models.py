from django.db import models

# Create your models here.

class Category(models.Model):
    ACTIVE = 'Active'
    DRAFT = 'Draft'

    CHOICE_STATUS = (
        (ACTIVE,'Active'),
        (DRAFT,'Draft')
                     )
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    status = models.CharField(max_length=10,choices=CHOICE_STATUS, default=ACTIVE)

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return f"{self.slug}"



    
class Post(models.Model):
    
    ACTIVE = 'Active'
    DRAFT = 'Draft'

    CHOICE_STATUS = (
        (ACTIVE,'Active'),
        (DRAFT,'Draft')
                     )
    category = models.ForeignKey(Category,related_name="category",on_delete=models.SET_NULL,null=True,)
    author = models.CharField(max_length=250)
    slug = models.SlugField()
    title = models.CharField(max_length=200)
    header_image = models.ImageField(upload_to="images/",null=True,blank=True)
    intro = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=CHOICE_STATUS, default=ACTIVE)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ("-created_at",)

    def get_absolute_url(self):
        return f"{self.slug}"

class Comment(models.Model):
    post = models.ForeignKey(Post,related_name="comments",on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.name} - {self.body} "
    
    class Meta:
        ordering = ("-created_at",)

class Member(models.Model):
    first_Name = models.CharField(max_length=100)
    last_Name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to="myapp/images/",)
    # header_image = models.ImageField(upload_to="images/",null=True,blank=True)
    position = models.CharField(max_length=100)
    facebook =  models.URLField(blank=True,null=True)
    twitter =  models.URLField(blank=True,null=True)
    instagram =  models.URLField(blank=True,null=True)
    linkedin =  models.URLField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.first_Name  + ' ' +  self.last_Name
    
    class Meta:
        ordering = ("created_at",)

class Testimonial(models.Model):

    profile_picture = models.ImageField(upload_to='testimonial/')
    client_name = models.CharField(max_length=25)
    profession = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.client_name 
    class Meta:
        ordering = ("-created_at",)