from django.shortcuts import render
from .models import gameList, gameDetails

# Create your views here.
def index(request):
    games = gameList.objects.all()
    return render(request, "index.html", {'games' : games})

def details(request):
    if request.method == "POST":
        selection = request.POST.get('Selection','')
        gDetail  = gameDetails.objects.get(gameID=selection)
        gSelect = gameList.objects.get(gameID=selection)
        gName = gSelect.gameName
        return render(request, "details.html", {'gDetail' : gDetail, 'gName' : gName})
    return render(request, "details.html")