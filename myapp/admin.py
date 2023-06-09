from django.contrib import admin
from .models import Post,Category,Message,Comment,Member,Testimonial,Contact
# Register your models here.


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["name","email","subject","body"]
    list_filter = ["created_at","name"]
    search_fields = ["name","email","subject"]


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ["name","email","service","message"]
    list_filter = ["created_at","name","email"]
    search_fields = ["name","email","subject"]




@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # "header_image",
    list_display = ["author","title","intro","body","created_at","intro"]
    search_fields = ["title","body","created_at"]
    prepopulated_fields = {"slug":["title"]}
    list_filter = ["created_at","author","category","status"]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title"]
    list_filter = ["status"]
    

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["name","email","body"]


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ["first_Name","last_Name"]

@admin.register(Testimonial)
class Testimonial(admin.ModelAdmin):
    search_fields = ["client_name","created_at"]
    list_display = ['client_name','content']










