from django.shortcuts import render

# Create your views here.
def listaMeta(request):
    return render(request, 'metas/lista.html')
