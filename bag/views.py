from django.shortcuts import render, redirect

# Create your views here.

def view_bag(request):
    """ A view renders the bag contents page """
    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cover = None
    if 'product_cover' in request.POST:
        cover = request.POST['product_cover']
    bag = request.session.get('bag', {})

    if cover:
        if item_id in list(bag.keys()):
            if cover in bag[item_id]['items_by_cover_type'].keys():
                bag[item_id]['items_by_cover_type'][cover] += quantity
            else:
                bag[item_id]['items_by_cover_type'][cover] = quantity
        else:
            bag[item_id] = {'items_by_cover_type': {cover: quantity}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] == quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)