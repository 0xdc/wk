from django.shortcuts import get_object_or_404,render,redirect
from django.http import HttpResponse
from django.contrib.staticfiles.templatetags.staticfiles import static

from .models import WellKnown

def view(request, tgt):
    wk = get_object_or_404(WellKnown, key__exact=tgt)
    return HttpResponse(wk.value, content_type="text/plain")

def wkd(request, tgt):
    return redirect(static( '/'.join(['wk','openpgpkey','hu', tgt]) ))
