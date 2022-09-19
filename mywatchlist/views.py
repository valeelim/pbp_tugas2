from django.views import generic
from mywatchlist.models import MyWatchList

from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize('xml', data), content_type='application/xml')

class IndexView(generic.ListView):
    template_name = 'mywatchlist.html'
    context_object_name = 'mywatchlist'

    def get_queryset(self):
        return list(MyWatchList.objects.all())
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'mywatchlist': list(MyWatchList.objects.all()),
            'nama': 'Valerian Salim',
            'npm': '2106630012',
            'msg': 'Selamat, kamu sudah banyak menonton!' if 2*sum([i.watched for i in context['mywatchlist']]) >= len(context['mywatchlist']) else 'Wah, kamu masih sedikit menonton!'
        })
        return context


