from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render,get_list_or_404,redirect
from .models import Post,Category,Comment,Member, Testimonial
from django.core.mail import send_mail,BadHeaderError

# categories = Category.objects.filter(status = Category.ACTIVE ).get(slug= category_slug)
# Create your views here.
def index(request):
    post = Post.objects.all()
    slice = post[:3]
    testimonial = Testimonial.objects.all()
    return render(request,"myapp/index.html",{'posts': slice,'testimonials':testimonial})

def about(request):
    return render(request,"myapp/about.html")

def contact(request):
    if request.method == "POST":

        message_name = request.POST['name']
        message_subject = request.POST['subject']
        message_email = request.POST['email']
        message = request.POST['message']

        # print(message_name,message_email,message)
        # send email
        if message_subject and message and message_email:
            # try:
                send_mail(
                message_subject,
                 message,
                 message_email,
                ['jahsconnection@gmail.com','adekunleakinwale2018@gmail.com'],
                fail_silently=False)
                return redirect('contact')
            # except BadHeaderError:
                # return  HttpResponse("Invalid header found")
            # return redirect('/contact/thanks/')
        else:
            return HttpResponse('Make sure all fields are entered and valid.')
    return render(request,"myapp/contact.html")

def service(request):
    return render(request,"myapp/service.html")

def team(request):
    member = Member.objects.all()
    return render(request,"myapp/team.html",{'members': member})

def testimonial(request):
    testimonial = Testimonial.objects.all()
    return render(request,"myapp/testimonial.html",{'testimonial': testimonial})

def blog(request):
    post = Post.objects.all()
    post = Post.objects.filter(status= Post.ACTIVE)
    
    return render(request,"myapp/blog.html",{"Posts":post})

def categories(request, category_slug):
    categories = Category.objects.filter(status = Category.ACTIVE ).get(slug= category_slug)
    

def price(request):
    
    return render(request,"myapp/price.html")

def detail(request,slug):
    post = Post.objects.get(slug=slug)
    if request.method == "POST":
       comment = Comment()
       comment.name  = request.POST["name"]
       comment.email  = request.POST["email"]
       comment.body  = request.POST["body"]
       comment.post = post
       comment.save()
       return redirect('detail',slug= slug)
    return render(request,"myapp/detail.html" ,{"post":post})


def search(request):
    query = request.GET.get("query",'')
    result = Post.objects.filter(status = Post.ACTIVE).filter(Q(title__icontains = query) | Q(intro__icontains = query)|Q(body__icontains = query))
    return render(request,"myapp/search.html",{"query":query,"results":result})

def story(request):
    return render(request,'myapp/story.html',{})


def career(request):
    return render(request,'myapp/career.html',{})



def feature(request):
    return render(request,'myapp/feature.html',{})