from django.shortcuts import render, get_object_or_404

from products.models import Product, Category
from reviews.models import Review

# Create your views here.

def index(request):
    """ A view to return the index page """

    classics = Product.objects.filter(category=1)[:4]
    classics_category = get_object_or_404(Category, pk=1)
    fiction = Product.objects.filter(category=2)[:4]
    fiction_category = get_object_or_404(Category, pk=2)
    non_fiction = Product.objects.filter(category=3)[:4]
    non_fiction_category = get_object_or_404(Category, pk=3)
    fantasy = Product.objects.filter(category=4)[:4]
    fantasy_category = get_object_or_404(Category, pk=4)
    journals_and_planners = Product.objects.filter(category=5).order_by("-isbn")[:4]
    journals_and_planners_category = get_object_or_404(Category, pk=5)
    notebooks = Product.objects.filter(category=6).order_by("-isbn")[:4]
    notebooks_category = get_object_or_404(Category, pk=6)
    reviews = Review.objects.all().order_by("-date")[:4]

    book_categories = [
        {
            'category': classics_category,
            'products': classics,
        },
        {
            'category': fiction_category,
            'products': fiction,
        },
        {
            'category': non_fiction_category,
            'products': non_fiction,
        },
        {
            'category': fantasy_category,
            'products': fantasy,
        },
    ]

    stationery_categories = [
        {
            'category': journals_and_planners_category,
            'products': journals_and_planners,
        },
        {
            'category': notebooks_category,
            'products': notebooks,
        },
    ]

    context = {
        'book_categories': book_categories,
        'stationery_categories': stationery_categories,
        'reviews': reviews,
    }

    return render(request, 'home/index.html', context)