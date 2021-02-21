from django.shortcuts import get_object_or_404,render,redirect
from django.http import HttpResponse
try:
    from django.contrib.staticfiles.templatetags.staticfiles import static
except ImportError:
    from django.templatetags.static import static

from .models import WellKnown

def view(request, tgt):
    wk = get_object_or_404(WellKnown, key__exact=tgt)
    return HttpResponse(wk.value, content_type="text/plain")

def wkd(request, tgt):
    return redirect(
            request.build_absolute_uri(
                static( '/'.join(['wk','openpgpkey','hu', tgt]) )
            )
    )
