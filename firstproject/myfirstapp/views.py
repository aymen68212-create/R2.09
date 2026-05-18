from django.shortcuts import render

def index(request):
    return render(request, 'myfirstapp/index.html')

def formulaire(request):
    return render(request, 'myfirstapp/formulaire.html')

def bonjour(request):
    context = {
        "nom": request.GET.get("nom"),
        "prenom": request.GET.get("prenom"),
        "age": request.GET.get("age"),
    }
    return render(request, 'myfirstapp/bonjour.html', context)