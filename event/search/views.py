from django.shortcuts import render
from eventapp.models import Event
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
@login_required
def search(request):
    query = ""
    e = None
    if (request.method == "POST"):
        query = request.POST['q']
        if (query):
            e = Event.objects.filter(Q(name__icontains=query) | Q(desc__icontains=query))
    return render(request, 'search.html', {'query': query, 'e': e})