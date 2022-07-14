from django.shortcuts import render
from .models import Review

# Create your views here.
def home(request):
    reviews = Review.objects.all()

    context = {
        "reviews" : reviews
    }

    return render(request, template_name="reviews/home.html", context=context)