from django.shortcuts import render

# Create your views here.


def board(request):
    return render((request), 'boards/boards.html')
