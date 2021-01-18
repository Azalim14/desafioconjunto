from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Meta
from .forms import *
from django.http import HttpResponse

# Create your views here.

@login_required
def listaMeta(request):

    search = request.GET.get('search')

    if search:

        metas = Meta.objects.filter(title__icontains=search)

    else:

        lista_metas = Meta.objects.all().order_by('-created_at')

        paginator = Paginator(lista_metas, 5)

        page = request.GET.get('page')

        metas = paginator.get_page(page)

    return render(request, 'metas/lista.html', {'metas': metas})

@login_required
def metaView(request, id):
    meta = get_object_or_404(Meta, pk=id)
    return render(request, 'metas/meta.html', {'meta': meta})

@login_required
def novaMeta(request):
    if request.method == 'POST':
        form = NovaMetaForm(request.POST)
        if form.is_valid():
            meta = form.save(commit=False)
            meta.done = 'doing'
            meta.save()
            return redirect('/')
        else:
            return HttpResponse('uai')
    else:
        form = NovaMetaForm()
        return render(request, 'metas/novameta.html', {'form': form})

@login_required
def editMeta(request, id):
    meta = get_object_or_404(Meta, pk=id)
    form = NovaMetaForm(instance=meta)

    if request.method == 'POST':
        form = NovaMetaForm(request.POST, instance=meta)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, 'metas/editmeta.html', {'form': form, 'meta': meta})
    else:
        return render(request, 'metas/editmeta.html', {'form': form, 'meta': meta})

@login_required
def deleteMeta(request,id):
    meta = get_object_or_404(Meta, pk=id)
    meta.delete()
    return redirect('/')
