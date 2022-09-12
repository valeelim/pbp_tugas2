from django.views import generic
from .models import CatalogItem

# TODO: Create your views here.

class IndexView(generic.ListView):
    template_name = 'katalog.html'
    context_object_name = 'katalog_list'

    def get_queryset(self):
        return CatalogItem.objects.all()
