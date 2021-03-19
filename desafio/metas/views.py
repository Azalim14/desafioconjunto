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

        metas = Meta.objects.filter(title__icontains=search, deletado=False)

    elif filter:

        metas = Meta.objects.filter(done=filter, deletado=False)

    else:

        lista_metas = Meta.objects.filter(deletado=False).order_by('-created_at')

        for meta in lista_metas:
            entrega = meta.entrega
            criada = meta.created_at
            hoje = datetime.date.today()
            dias_total = abs((entrega - criada).days)
            dias = abs((entrega - hoje).days)

            if meta.done == 'doing':
                if dias <= (dias_total * 0.1) or hoje > entrega:
                    meta.semaforo = 'vermelho'
                    meta.save()
                elif dias > (dias_total * 0.1) and dias <= (dias_total * 0.4):
                    meta.semaforo = 'amarelo'
                    meta.save()
                else:
                    meta.semaforo = 'azul'
                    meta.save()

        paginator = Paginator(lista_metas, 3)

        page = request.GET.get('page')

        metas = paginator.get_page(page)



    data = {
        'metas': metas,
    }

    return render(request, 'metas/lista.html', data)

def metaView(request, id):
    meta = get_object_or_404(Meta, pk=id)

    comentarios = Comentario.objects.filter(fk_meta = meta).order_by('-created_at')

    entrega = meta.entrega
    criada = meta.created_at
    hoje = datetime.date.today()
    dias_total = abs((entrega - criada).days)
    dias = abs((entrega - hoje).days)

    if meta.done == 'doing':
        if dias <= (dias_total * 0.1) or hoje > entrega:
            meta.semaforo = 'vermelho'
            meta.save()
        elif dias > (dias_total * 0.1) and dias <= (dias_total * 0.4):
            meta.semaforo = 'amarelo'
            meta.save()
        else:
            meta.semaforo = 'azul'
            meta.save()

    return render(request, 'metas/meta.html', {'meta': meta, 'comentarios': comentarios})

def novaMeta(request):
    if request.method == 'POST':
        form = NovaMetaForm(request.POST)
        if form.is_valid():
            meta = form.save(commit=False)
            meta.done = 'doing'
            meta.deletado = False
            meta.porcentagem = 0
            meta.semaforo = 'azul'
            meta.save()
            return redirect('/')
    else:
        form = NovaMetaForm()
        return render(request, 'metas/novameta.html', {'form': form})

def novaMetaSetor(request, setorP):
    if request.method == 'POST':
        setor = get_object_or_404(Setor, ident=setorP)
        form = NovaMetaSetorForm(request.POST)
        if form.is_valid():
            meta = form.save(commit=False)
            meta.done = 'doing'
            meta.deletado = False
            meta.porcentagem = 0
            meta.setor = setor
            meta.semaforo = 'azul'
            meta.save()
            return redirect('/' + setor.ident)
    else:
        setor = get_object_or_404(Setor, ident=setorP)
        form = NovaMetaSetorForm()
        return render(request, 'metas/novameta.html', {'form': form, 'setor': setor.name})

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

def deleteMeta(request, id):
    meta = get_object_or_404(Meta, pk=id)
    meta.deletado = True
    meta.save()
    return redirect('/')

@login_required
def deletaMesmo(request, id):
    meta = get_object_or_404(Meta, pk=id)
    meta.delete()
    return redirect('/deletadas/')

def activateMeta(request, id):
    meta = get_object_or_404(Meta, pk=id)
    meta.deletado = False
    meta.save()
    return redirect('/')

def changeStatus(request, id):
    meta = get_object_or_404(Meta, pk=id)

    if meta.done == 'doing':
        meta.done = 'done'
        meta.semaforo = 'verde'
        meta.save()
        return redirect('/comentario/' + str(meta.id) + '/100')
    else:
        meta.done = 'doing'
        meta.semaforo = 'azul'
        meta.save()
        return redirect('/')

def changeStatusCor(request, id):
    meta = get_object_or_404(Meta, pk=id)

    if meta.done == 'doing':
        meta.done = 'done'
        meta.semaforo = 'verde'
        meta.save()
        return redirect('/comentario/' + str(meta.id) + '/100')
    else:
        meta.done = 'doing'
        meta.semaforo = 'azul'
        meta.save()
        return redirect('/metas/' + str(meta.semaforo ))

def changeStatusS(request, id):
    meta = get_object_or_404(Meta, pk=id)

    if meta.done == 'doing':
        meta.done = 'done'
        meta.semaforo = 'verde'
        meta.save()
        return redirect('/comentario/' + str(meta.id) + '/100')
    else:
        meta.done = 'doing'
        meta.semaforo = 'azul'
        meta.save()
        return redirect('/' + str(meta.setor.ident))

def changeStatusCSComentario(request, id, porcentagem):
    meta = get_object_or_404(Meta, pk=id)

    if meta.done == 'doing':
        meta.done = 'done'
        meta.semaforo = 'verde'
        meta.porcentagem = 100
        meta.save()
        return redirect('/' + str(meta.setor.ident))
    else:
        meta.done = 'doing'
        meta.semaforo = 'azul'
        meta.save()
        return redirect('/' + str(meta.setor.ident))

def changeStatusSSComentario(request, id, porcentagem):
    meta = get_object_or_404(Meta, pk=id)

    if meta.done == 'doing':
        meta.done = 'done'
        meta.semaforo = 'verde'
        meta.porcentagem = 100
        meta.save()
        return redirect('/' + str(meta.setor.ident))
    else:
        meta.done = 'doing'
        meta.semaforo = 'azul'
        meta.save()
        return redirect('/' + str(meta.setor.ident))

def changeStatusSComentario(request, id, porcentagem):
    meta = get_object_or_404(Meta, pk=id)

    if meta.done == 'doing':
        meta.done = 'done'
        meta.semaforo = 'verde'
        meta.porcentagem = 100
        meta.save()
        return redirect('/meta/' + str(meta.id))
    else:
        meta.done = 'doing'
        meta.semaforo = 'azul'
        meta.save()
        return redirect('/meta/' + str(meta.id))
    

def home(request):

    setores = Setor.objects.all().order_by('name')
    lista_metas = Meta.objects.filter(deletado=False).order_by('-created_at')
    concluidas = len(Meta.objects.filter(done='done', deletado=False))
    em_progresso = len(Meta.objects.filter(semaforo='azul', deletado=False))
    atrasadas = len(Meta.objects.filter(semaforo='vermelho', deletado=False))
    atencao = len(Meta.objects.filter(semaforo='amarelo', deletado=False))
    if len(lista_metas) != 0:
        porcentagem = concluidas/len(lista_metas)*100
    else:
        porcentagem = 0
    
    for meta in lista_metas:
        entrega = meta.entrega
        criada = meta.created_at
        hoje = datetime.date.today()
        dias_total = abs((entrega - criada).days)
        dias = abs((entrega - hoje).days)

        if meta.done == 'doing':
            if dias <= (dias_total * 0.1) or hoje > entrega:
                meta.semaforo = 'vermelho'
                meta.save()
            elif dias > (dias_total * 0.1) and dias <= (dias_total * 0.4):
                meta.semaforo = 'amarelo'
                meta.save()
            else:
                meta.semaforo = 'azul'
                meta.save()

    data = {
        'total_metas': len(lista_metas),
        'metas': lista_metas,
        'setores': setores,
        'data': datetime.date.today(),
        'concluidas': concluidas,
        'progresso': em_progresso,
        'atrasadas': atrasadas,
        'atencao': atencao,
        'porcentagem': round(porcentagem,1),
        'qs': lista_metas,
    }

    return render(request, 'metas/home.html', data)

def alterandoPorcentagem(request, id, porcentagem):
    meta = get_object_or_404(Meta, pk=id)
    form = NovoComentarioForm(request.POST)
    
    if request.method == 'POST':
        form = NovoComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.fk_meta = meta
            comentario.save()
            meta.porcentagem = porcentagem
            meta.save()
            return redirect('/meta/' + str(meta.id))
        else:
            return render(request, 'metas/novocomentario.html', {'form': form})
    else:
        return render(request, 'metas/novocomentario.html', {'form': form})

        
@login_required
def listaDeletadas(request):

    search = request.GET.get('search')
    filter = request.GET.get('filter')

    if search:

        metas = Meta.objects.filter(title__icontains=search, deletado=True)

    elif filter:

        metas = Meta.objects.filter(done=filter, deletado=True)

    else:

        lista_metas = Meta.objects.filter(deletado=True).order_by('-created_at')

        paginator = Paginator(lista_metas, 5)

        page = request.GET.get('page')

        metas = paginator.get_page(page)

    data = {
        'metas': metas,
    }

    return render(request, 'metas/listaDeletadas.html', data)

def listaSetor(request, setorLista):

    setorFiltro = get_object_or_404(Setor, ident=setorLista)
    search = request.GET.get('search')
    filter = request.GET.get('filter')

    if search:

        metas = Meta.objects.filter(title__icontains=search, setor=setorFiltro)

    elif filter:

        metas = Meta.objects.filter(setor=setorFiltro, done=filter)

    else:

        lista_metas = Meta.objects.filter(setor=setorFiltro, deletado=False).order_by('-created_at')

        paginator = Paginator(lista_metas, 3)

        page = request.GET.get('page')

        metas = paginator.get_page(page)

    data = {
        'metas': metas,
        'setor': setorFiltro,
    }

    return render(request, 'metas/listasetor.html', data)

def listaCor(request, cor):

    search = request.GET.get('search')
    filter = request.GET.get('filter')

    if search:

        metas = Meta.objects.filter(title__icontains=search, semaforo=cor)

    elif filter:

        metas = Meta.objects.filter(semaforo=cor, done=filter)

    else:

        lista_metas = Meta.objects.filter(semaforo=cor, deletado=False).order_by('-created_at')

        paginator = Paginator(lista_metas, 3)

        page = request.GET.get('page')

        metas = paginator.get_page(page)

    data = {
        'metas': metas,
        'cor': cor,
    }

    return render(request, 'metas/listacor.html', data)

def sobre(request):
    return render(request, 'metas/sobre.html')
