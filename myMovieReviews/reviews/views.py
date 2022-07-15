from django.shortcuts import redirect, render

from reviews.movie_info import searchInfo
from .models import Review

# Create your views here.
def home(request):
    sort = request.GET.get('sort','')
    if sort == '':
        reviews = Review.objects.all()
    else:
        reviews = Review.objects.all().order_by(sort)
    context = {
        "reviews" : reviews
    }

    return render(request, template_name="reviews/home.html", context=context)

def create(request):
    if request.method == "POST":
        title = request.POST["title"]
        release = request.POST["release"]
        genre = request.POST["genre"]
        star = request.POST["star"]
        time = request.POST["time"]
        content = request.POST["content"]
        director = request.POST["director"]
        actor = request.POST["actor"]
        img = request.POST["img"]
        poster = request.POST["poster"]

        Review.objects.create(title=title, release=release, genre=genre, star=star, time=time, content=content, director=director, actor=actor, img=img ,poster=poster)
        return redirect("/")
    
    else:
        title = request.GET.get("title")
        release = request.GET.get("release")
        genre = request.GET.get("genre")
        time = request.GET.get("time")
        director = request.GET.get("director")
        actor = request.GET.get("actor")
        img = request.GET.get("img")
        poster = request.GET.get("poster")

        if title == None:
            context = {}
        else:
            context = {
            'title':title,
            'release':release, 
            'genre':genre, 
            'time':time, 
            'director':director, 
            'actor':actor,
            'img':img,
            'poster':poster,
        }
        return render(request, template_name="reviews/create.html", context=context)

def search(request):
    if request.method == "POST":
        title = request.POST["title"]
        results = searchInfo(title)
        if results:
            context = {
            "results" : results
            }
            return render(request, template_name="reviews/search.html", context = context)
        else:
            context = {}
            return render(request, template_name="reviews/search.html", context = context)

def detail(request, id):
    review = Review.objects.get(id=id)
    
    context = {
        "review" : review
    }

    return render(request, template_name="reviews/detail.html", context=context)

def modify(request, id):
    if request.method == "POST":
        title = request.POST["title"]
        release = request.POST["release"]
        genre = request.POST["genre"]
        star = request.POST["star"]
        time = request.POST["time"]
        content = request.POST["content"]
        director = request.POST["director"]
        actor = request.POST["actor"]
        
        Review.objects.filter(id=id).update(title=title, release=release, genre=genre, star=star, time=time, content=content, director=director, actor=actor)
        return redirect(f"/review/{id}")
    else:
        review = Review.objects.get(id=id)
        context = {
            "review" : review
        }
        return render(request, template_name="reviews/modify.html", context=context)


def delete(request, id):
    if request.method == "POST":
        Review.objects.filter(id=id).delete()
    return redirect("/")