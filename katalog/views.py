from django.views import generic
from .models import CatalogItem

# TODO: Create your views here.

class IndexView(generic.ListView):
    template_name = 'katalog.html'
    context_object_name = 'katalog_list'
    
    def get_queryset(self):
        return CatalogItem.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'katalog_list': CatalogItem.objects.all(),
            'nama': 'Valerian Salim',
            'npm': '2106630012'
        })
        return context        
