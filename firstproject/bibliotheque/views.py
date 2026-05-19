from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import LivreForm
from . import models

def ajout(request):
    if request.method == "POST":
        form = LivreForm(request.POST)
        if form.is_valid():
            Livre = form.save()
            return render(request, "bibliotheque/affiche.html", {"Livre": Livre})
        else:
            return render(request, "bibliotheque/ajout.html", {"form": form})
    else:
        form = LivreForm()
        return render(request, "bibliotheque/ajout.html", {"form": form})

def traitement(request):
    lform = LivreForm(request.POST)
    if lform.is_valid():
        Livre = lform.save()
        return render(request, "bibliotheque/affiche.html", {"Livre": Livre})
    else:
        return render(request, "bibliotheque/ajout.html", {"form": lform})

def all(request):
    livres = list(models.Livre.objects.all())
    return render(request, "bibliotheque/all.html", {"livres": livres})

def read(request, id):
    Livre = models.Livre.objects.get(pk=id)
    return render(request, "bibliotheque/affiche.html", {"Livre": Livre})

def update(request, id):
    Livre = models.Livre.objects.get(pk=id)
    form = LivreForm({
        'titre': Livre.titre,
        'auteur': Livre.auteur,
        'date_parution': Livre.date_parution,
        'nombre_pages': Livre.nombre_pages,
        'resume': Livre.resume,
    })
    return render(request, "bibliotheque/update.html", {"form": form, "id": id})

def traitementupdate(request, id):
    lform = LivreForm(request.POST)
    if lform.is_valid():
        Livre = lform.save(commit=False)
        Livre.id = id
        Livre.save()
        return HttpResponseRedirect("/bibliotheque/")
    else:
        return render(request, "bibliotheque/update.html", {"form": lform, "id": id})

def delete(request, id):
    Livre = models.Livre.objects.get(pk=id)
    Livre.delete()
    return HttpResponseRedirect("/bibliotheque/")