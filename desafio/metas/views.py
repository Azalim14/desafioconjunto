from django.shortcuts import render, get_object_or_404
from .models import Meta

# Create your views here.
def listaMeta(request):
    metas = Meta.objects.all()
    return render(request, 'metas/lista.html', {'metas': metas})

def metaView(request, id):
    meta = get_object_or_404(Meta, pk=id)
    return render(request, 'metas/meta.html', {'meta': meta})
 