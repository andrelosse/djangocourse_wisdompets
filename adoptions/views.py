from django.shortcuts import render
from django.http import Http404

from .models import Pets

def index (request):
    pets = Pets.objects.all()

    return render(request, 'index.html', {'pets': pets,})

def pet_details (request, pet_id):

    try:
        pet = Pets.objects.get(id=pet_id)
    except Pets.DoesNotExist:
        raise Http404('Pet does not exist...')
    
    return render(request, 'pet_details.html', {'pet': pet,})