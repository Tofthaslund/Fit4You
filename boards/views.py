from django.shortcuts import render

from django.views.generic import ListView


from .models import Board


class BoardListView(ListView):
    Model = Board
    Context_object_name = 'boards'
    template_name = 'boards/boards.html'
