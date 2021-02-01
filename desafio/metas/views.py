from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Meta
from .forms import *
from django.http import HttpResponse
import datetime

# Create your views here.

@login_required
def listaMeta(request):

    search = request.GET.get('search')
    filter = request.GET.get('filter')

    if search:

        metas = Meta.objects.filter(title__icontains=search, user=request.user)

    elif filter:

        metas = Meta.objects.filter(done=filter, user=request.user)

    else:

        lista_metas = Meta.objects.all().order_by('-created_at').filter(user=request.user)

        paginator = Paginator(lista_metas, 5)

        page = request.GET.get('page')

        metas = paginator.get_page(page)

    data = {
        'metas': metas,
    }

    return render(request, 'metas/lista.html', data)

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
            meta.user = request.user
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

@login_required
def changeStatus(request, id):
    meta = get_object_or_404(Meta, pk=id)

    if meta.done == 'doing':
        meta.done = 'done'
    else:
        meta.done = 'doing'

    meta.save()

    return redirect('/')

@login_required
def home(request):

    metasDoneRecently = Meta.objects.filter(user=request.user, done='done', updated_at__gt=datetime.datetime.now()-datetime.timedelta(days=30)).count()
    metasDoing = Meta.objects.filter(done='doing', user=request.user).count()
    metasDone = Meta.objects.filter(done='done', user=request.user).count()
    lista_metas = Meta.objects.all().order_by('-created_at').filter(user=request.user)[:3]

    data = {
        'metasrecently': metasDoneRecently,
        'metasdone': metasDone,
        'metasdoing': metasDoing,
        'metas' : lista_metas,
    }

    return render(request, 'metas/home.html', data)
