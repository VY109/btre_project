from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from listings.choices import price_choices, bedroom_choices, state_choices
# already in listings app so just .choices will do
from .choices import price_choices, bedroom_choices, state_choices

# fetch from db and populate to listings.html
from .models import Listing


# return the render
# optional [pass in values into the template using dictionary]
# -- then goto listings.html and output using {{name}}
# 2nd preferred way is to create a variable with dictionary and pass that in
def index(request):
    # but not our name, fetch the listing from the dbase
    #  pip install pylint-django if the linter complains abt Listing having no objects member
    # listings = Listing.objects.all()  - is descending
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    # 6 per page
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        # 'listings': listings
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)
    # return render(request, 'listings/listings.html',{
    #     'name': 'Yeon'
    # })

# when listing id is in listings.html, pass the id in here for the route
# 'more info' from featured listing
def listing(request, listing_id):
    # from urls.py -- path('<int:listing_id>'
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)

def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    # keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            # query the description field __ dbl underscore field contains..
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # city
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            # query the description field __ dbl underscore field equals iexact = case insensitive 
            queryset_list = queryset_list.filter(city__iexact=city)    

    # state
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            # query the description field __ dbl underscore field equals iexact = case insensitive 
            queryset_list = queryset_list.filter(state__iexact=state)  

    # bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            # query the description field __ dbl underscore field lte = less than or equal to
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)  

    # price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            # query the description field __ dbl underscore field lte = less than or equal to
            queryset_list = queryset_list.filter(price__lte=price)  


    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': queryset_list,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)