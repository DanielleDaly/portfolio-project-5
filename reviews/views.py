from django.shortcuts import render, get_object_or_404

from .models import Review


def all_reviews(request):
    """ A view to show all reviews """

    reviews = Review.objects.all()

    context = {
        'reviews': reviews,
    }

    return render(request, 'reviews/reviews.html', context)


def review(request, review_id):
    """ A view to show review """

    review = get_object_or_404(Review, pk=review_id)

    context = {
        'review': review,
    }

    return render(request, 'reviews/review.html', context)
