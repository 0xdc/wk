from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse

from .models import WellKnown

def view(request, tgt):
    wk = get_object_or_404(WellKnown, key__exact=tgt)
    return HttpResponse(wk.value)
