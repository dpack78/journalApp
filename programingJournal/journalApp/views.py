from django.shortcuts import render
from django.views import generic
from django.views.generic import DetailView
from .models import Entry
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from itertools import chain
import pdb
# Create your views here.

# class IndexView():
#     model = Entry
#     slug_field = 'entry'
#     template_name = 'journalApp/index.html'
#     # context_object_name = 'lastEntry'
#     # newest_entry = Entry.objects.latest('creation_date')
#
#     # def getMostRecentEntry():
#         # return Entry.objects.filter('field')
#     def get_queryset(self):
#         return Entry.objects.latest('creation_date')

# def saveCodeSession(request):

def index(request):
    newest_entry = Entry.objects.latest('creation_date')
	all_entries = Entry.objects.all()
    context = { 'newest_entry': newest_entry,
				'all_entries' : all_entries
	}
    return render(request, 'journalApp/index.html',context)

def saveNewDay(request):
    entry = Entry()
    # pdb.set_trace()
    entry.creation_date = timezone.now()
    entry.page_name = request.GET['curPage']
    # ('curPage',"None")
    entry.line_number = request.GET['lineNumber']
    # ('lineNumber',-1)
    entry.working_on = request.GET['currentThoughts']
    # ('currentThoughts',"None")
    entry.goals = request.GET['goals']
    # ('goals',"No Goals")
    entry.save()
    return HttpResponseRedirect('/')
