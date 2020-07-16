from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Item
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

app_name = 'core'


# view for homepage
def index(request):
    return render(request, 'core/index.html')


# view for business page
def business(request):
    return render(request, 'core/business.html')


# view for about page
def about(request):
    return render(request, 'core/about.html')


# view for product categories
# class CategoryView(ListView):
#     model = Item
#     context_object_name = 'items'
#     template_name = 'core/category.html'
#     paginate_by = 1
#     queryset = Item.objects.all().filter(category='C').order_by('-id')

    # def get_queryset(self):
    #     queryset = {
    #         'animals': Item.objects.all().filter(category='A'),
    #         'crops': Item.objects.all().filter(category='C'),
    #         'services': Item.objects.all().filter(category='S')
    #     }
    #     return queryset


def catview(request):
    crops = Item.objects.all().filter(category='C').order_by('id')
    animals = Item.objects.all().filter(category='A').order_by('id')
    services = Item.objects.all().filter(category='S').order_by('id')

    page = request.GET.get('page', 1)
    paginator = Paginator(crops, 1)

    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    users = paginator.get_page(page)

    return render(request, 'core/category.html', {'crops': crops,
                                                  'animals': animals,
                                                  'services': services,
                                                  'users': users
                                                  })


# view for single product page
class ItemDetailView(DetailView):
    model = Item
    template_name = 'core/product.html'


# view for contact page
def contact(request):
    return render(request, 'core/contact.html')
