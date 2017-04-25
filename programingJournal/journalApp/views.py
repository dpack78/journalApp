from django.shortcuts import render
from django.views import generic
from django.views.generic import DetailView
from .models import Entry
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
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
    newest_entry = Entry.objects.latest('creation_date');
    context = { 'newest_entry': newest_entry}
    return render(request, 'journalApp/index.html',context)
