from django.shortcuts import render
from .models import Review

# Create your views here.
def home(request):
    reviews = Review.objects.all()

    context = {
        "reviews" : reviews
    }

    return render(request, template_name="reviews/home.html", context=context)

def detail(request, id):
    review = Review.objects.get(id=id)

    context = {
        "review" : review
    }

    return render(request, template_name="reviews/detail.html", context=context)