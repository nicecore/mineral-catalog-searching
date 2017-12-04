from django.shortcuts import render, get_object_or_404
from .models import Mineral
import random
from django.forms.models import model_to_dict
import json
from django.db import IntegrityError


def mineral_list(request):
    """Return all minerals, plus a random mineral"""
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
    mineral = model_to_dict(mineral_predict)
    minerals = Mineral.objects.all()
    random_min = random.choice(minerals)
    return render(
        request,
        'minerals/mineral_detail.html',
        {'mineral': mineral, 'random': random_min}
    )


def search(request):
    """Search minerals by a term received from the user"""
    term = request.GET.get("q")
    minerals = Mineral.objects.filter(name__icontains=term)
    all_minerals = Mineral.objects.all()
    random_min = random.choice(all_minerals)
    return render(
        request,
        'minerals/mineral_list.html',
        {'minerals': minerals, 'random': random_min}
    )


def minerals_by_letter(request, letter):
    """Return minerals sorted by letter of the alphabet"""
    minerals = Mineral.objects.filter(name__istartswith=letter.lower())
    all_minerals = Mineral.objects.all()
    random_min = random.choice(all_minerals)
    return render(
        request,
        'minerals/mineral_list.html',
        {'minerals': minerals, 'active_letter': letter, 'random': random_min})


def minerals_by_group(request, group):
    """Return minerals by 'group' attribute"""
    minerals = Mineral.objects.filter(group=group)
    all_minerals = Mineral.objects.all()
    random_min = random.choice(all_minerals)
    return render(
        request,
        'minerals/mineral_list.html',
        {'minerals': minerals, 'random': random_min})
