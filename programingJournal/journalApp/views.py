from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.views.generic import DetailView
from .models import Entry
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from itertools import chain
import pdb
# Create your views here.

def index(request, pk = -1):
    entry_id = pk
    if entry_id != -1:
        newest_entry = get_object_or_404(Entry, pk=entry_id)
    else:
        newest_entry = Entry.objects.latest('creation_date')

    all_entries = Entry.objects.all()
    context = { 'newest_entry' : newest_entry,
                'all_entries' : all_entries
    }
    return render(request, 'journalApp/index.html',context)

def saveNewDay(request):
    entry = Entry()
    entry.creation_date = timezone.now()
    entry.page_name = request.GET['curPage']
    entry.line_number = request.GET['lineNumber']
    entry.working_on = request.GET['currentThoughts']
    entry.goals = request.GET['goals']
    entry.save()
    return HttpResponseRedirect('/')
