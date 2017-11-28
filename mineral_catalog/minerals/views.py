from django.shortcuts import render, get_object_or_404
from .models import Mineral
import random
from django.forms.models import model_to_dict
import json
from django.db import IntegrityError


def make_mineral_dict(mineral):
    """Make a dictionary out of a mineral object from JSON file"""
    fields = {
        'name': None,
        'image filename': None,
        'image caption': None,
        'category': None,
        'formula': None,
        'strunz classification': None,
        'crystal system': None,
        'unit cell': None,
        'color': None,
        'crystal symmetry': None,
        'cleavage': None,
        'mohs scale hardness': None,
        'luster': None,
        'streak': None,
        'diaphaneity': None,
        'optical properties': None,
        'refractive index': None,
        'crystal habit': None,
        'specific gravity': None
    }

    for key, value in mineral.items():
        fields[key] = value
    return fields


def add_minerals_to_database():
    """Uses preceding function to load mineral objects as dicts into the database."""
    with open('minerals.json', encoding='utf-8') as file:
        minerals = json.load(file)
        for mineral in minerals:
            try:
                fields = make_mineral_dict(mineral)
                Mineral(
                    name=fields['name'],
                    image_filename=fields['image filename'],
                    image_caption=fields['image caption'],
                    category=fields['category'],
                    formula=fields['formula'],
                    strunz_classification=fields['strunz classification'],
                    crystal_system=fields['crystal system'],
                    unit_cell=fields['unit cell'],
                    color=fields['color'],
                    crystal_symmetry=fields['crystal symmetry'],
                    cleavage=fields['cleavage'],
                    mohs_scale_hardness=fields['mohs scale hardness'],
                    luster=fields['luster'],
                    streak=fields['streak'],
                    diaphaneity=fields['diaphaneity'],
                    optical_properties=fields['optical properties'],
                    refractive_index=fields['refractive index'],
                    crystal_habit=fields['crystal habit'],
                    specific_gravity=fields['specific gravity']
                ).save()
            except IntegrityError:
                continue


def mineral_list(request):
    """Return all minerals, plus a random mineral"""
    add_minerals_to_database()
    minerals = Mineral.objects.all()
    random_min = random.choice(minerals)
    return render(
        request,
        'minerals/mineral_list.html',
        {'minerals': minerals, 'random': random_min}

    )


def mineral_detail(request, pk):
    """Return a particular mineral, plus a random mineral"""
    mineral_predict = get_object_or_404(Mineral, pk=pk)
    minerals = Mineral.objects.all()
    random_min = random.choice(minerals)
    mineral = model_to_dict(mineral_predict)
    return render(
        request,
        'minerals/mineral_detail.html',
        {'mineral': mineral, 'random': random_min}
    )


def search(request):
    term = request.GET.get("q")
    minerals = Mineral.objects.filter(name__icontains=term)
    return render(request, 'minerals/mineral_list.html', {'minerals': minerals})






