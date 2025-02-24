"""
Module contains the view for the sustainability page
"""
from django.shortcuts import render, redirect
from django.contrib import messages


def sustain(request):
    """Function that retrieves sustain.html"""
    return render(request, 'sustain.html')
