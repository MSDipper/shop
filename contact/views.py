from django.shortcuts import render
from django.views.generic import ListView
from contact.models import Contact


class ContactListView(ListView):
    model = Contact