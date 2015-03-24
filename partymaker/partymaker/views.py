from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from partymaker.models import AnimalRating, Animal, Neighborhood
from partymaker.forms import AnimalForm,NeighborhoodForm
import json
# Create your views here.

def welcome(request):
    return render(request, "welcome.html")

# Animals
####################################
def list_animals(request):
    return render(request, "animal_list.html", {"animals":Animal.objects.all()})

def list_animals_json(request):
    master = {}
    nodes_simple = []
    nodes_full = []
    links = []
    animals = Animal.objects.all()
    for animal in animals:
        if animal.email not in nodes_simple:
            nodes_simple.append(animal.email)
            nodes_full.append({"name":animal.email})
        animal_index = nodes_simple.index(animal.email)
        for rating in animal.get_ratings():
            if rating.ratee.email not in nodes_simple:
                nodes_simple.append(rating.ratee.email)
                nodes_full.append({"name":rating.ratee.email})
            ratee_index = nodes_simple.index(rating.ratee.email)
            links.append({"source":animal_index,"target":ratee_index,"value":rating.liking*30})
    master["nodes"] = nodes_full
    master["links"] = links
    return HttpResponse(json.dumps(master), content_type="application/json")

def view_animal(request,animal_id):
    animal = Animal.objects.get(pk=animal_id)
    form = AnimalForm(instance=animal)
    return render(request, "animal_view.html", {"form":form,"id":animal_id, "ratings":animal.get_ratings()})

def edit_animal(request,animal_id):
    if request.method == "POST":
        form = AnimalForm(request.POST)
        if form.is_valid():
            animal = Animal.objects.get(pk=animal_id)
            aform = AnimalForm(request.POST, instance=animal)
            aform.save()
            return HttpResponseRedirect("/animal/%d/" % animal.id)
        else:
            return render(request, "animal_view.html", {"form":form, "submitbutton":"Modify"})
    form = AnimalForm(instance=Animal.objects.get(pk=animal_id))
    return render(request, "animal_view.html", {"form":form, "submitbutton":"Update", "id":animal_id})

def create_animal(request):
    if request.method == "POST":
        form = AnimalForm(request.POST)
        if form.is_valid():
            animal = form.save(commit=False)
            animal.save()
            return HttpResponseRedirect("/animal/%d/" % animal.id)
        else:
            return render(request, "animal_view.html", {"form":form, "submitbutton":"Create"})
    form = AnimalForm()
    return render(request, "animal_view.html", {"form":form, "submitbutton":"Create"})


# Neighborhoods
####################################
def list_neighborhoods(request):
    return render(request, "neighborhood_list.html", {"neighborhoods":Neighborhood.objects.all()})

def view_neighborhood(request, neighborhood_id):
    form = NeighborhoodForm(instance=Neighborhood.objects.get(pk=neighborhood_id))
    return render(request, "neighborhood_view.html", {"animals":Neighborhood.objects.all(), "id":neighborhood_id})

def edit_neighborhood(request,neighborhood_id):
    if request.method == "POST":
        form = NeighborhoodForm(request.POST)
        if form.is_valid():
            neighborhood = Neighborhood.objects.get(pk=neighborhood_id)
            neighborhood = NeighborhoodForm(request.POST, instance=animal)
            aform.save()
            return HttpResponseRedirect("/neighborhood/%d/" % neighborhood_id)
        else:
            return render(request, "neighborhood_view.html", {"form":form, "submitbutton":"Modify"})
    form = NeighborhoodForm(instance=Neighborhood.objects.get(pk=neighborhood_id))
    return render(request, "neighborhood_view.html", {"form":form, "submitbutton":"Update", "id":neighborhood_id})

def create_neighborhood(request):
    if request.method == "POST":
        form = NeighborhoodForm(request.POST)
        if form.is_valid():
            neighborhood = form.save(commit=False)
            neighborhood.save()
            return HttpResponseRedirect("/animal/%d/" % neighborhood.id)
        else:
            return render(request, "animal_view.html", {"form":form, "submitbutton":"Create"})
    form = NeighborhoodForm()
    return render(request, "animal_view.html", {"form":form, "submitbutton":"Create"})

