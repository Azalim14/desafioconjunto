from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Meta
from .forms import *
from django.http import HttpResponse
import datetime

# Create your views here.

def listaMeta(request):

    search = request.GET.get('search')
    filter = request.GET.get('filter')

    if search:

        metas = Meta.objects.filter(title__icontains=search)

    elif filter:

        metas = Meta.objects.filter(done=filter)

    else:

        lista_metas = Meta.objects.all().order_by('-created_at')

        paginator = Paginator(lista_metas, 5)

        page = request.GET.get('page')

        metas = paginator.get_page(page)

    data = {
        'metas': metas,
    }

    return render(request, 'metas/lista.html', data)

def metaView(request, id):
    meta = get_object_or_404(Meta, pk=id)

    comentarios = Comentario.objects.filter(fk_meta = meta).order_by('-created_at')

    return render(request, 'metas/meta.html', {'meta': meta, 'comentarios': comentarios})

def novaMeta(request):
    if request.method == 'POST':
        form = NovaMetaForm(request.POST)
        if form.is_valid():
            meta = form.save(commit=False)
            meta.done = 'doing'
            meta.save()
            return redirect('/')
    else:
        form = NovaMetaForm()
        return render(request, 'metas/novameta.html', {'form': form})

def novoComentario(request, id):
    meta = get_object_or_404(Meta, pk=id)
    form = NovoComentarioForm(request.POST)

    if request.method == 'POST':
        form = NovoComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.fk_meta = meta
            comentario.save()
            return redirect('/meta/' + str(meta.id))
        else:
            return render(request, 'metas/novocomentario.html', {'form': form})
    else:
        return render(request, 'metas/novocomentario.html', {'form': form})

def editMeta(request, id):
    meta = get_object_or_404(Meta, pk=id)
    form = NovaMetaForm()

    if request.method == 'POST':
        form = NovaMetaForm(request.POST, instance=meta)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, 'metas/editmeta.html', {'form': form, 'meta': meta})
    else:
        return render(request, 'metas/editmeta.html', {'form': form, 'meta': meta})

def deleteMeta(request,id):
    meta = get_object_or_404(Meta, pk=id)
    meta.delete()
    return redirect('/')

def changeStatus(request, id):
    meta = get_object_or_404(Meta, pk=id)

    if meta.done == 'doing':
        meta.done = 'done'
    else:
        meta.done = 'doing'

    meta.save()

    return redirect('/')

def home(request):

    metasDoneRecently = Meta.objects.filter(done='done', updated_at__gt=datetime.datetime.now()-datetime.timedelta(days=30)).count()
    lista_metas = Meta.objects.all().order_by('-created_at')[:3]

    data = {
        'metasrecently': metasDoneRecently,
        'metas' : lista_metas,
    }

    return render(request, 'metas/home.html', data)
