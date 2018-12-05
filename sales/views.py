from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def sales_overview(request, client, week ):

    context = {
        "client": client,
        "week": week,
    }
    return render(request, 'sales/sales_overview.html', context)


