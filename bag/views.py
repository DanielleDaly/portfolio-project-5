from django.shortcuts import render

# Create your views here.

def view_bag(request):
    """ A view renders the bag contents page """
    return render(request, 'bag/bag.html')