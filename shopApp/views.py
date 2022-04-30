from django.shortcuts import  render, redirect
from .models import gameList, gameDetails
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

# Create your views here.
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})

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

def search(request):
    selected = ""
    criteria = ""
    ordering = ""
    asc_desc = ""
    hide = ""
    if request.method == "POST":
        search   = request.POST.get('selected','')
        criteria = request.POST.get('criteria','')
        ordering = request.POST.get('ordering','')
        asc_desc = request.POST.get('asc_desc','')
        results = ""
        results1 = ""
        hide ="Y"
        if asc_desc == "DESC":
            ordering = "-"+str(ordering)

        if search == "gameName":
            if criteria != "":
                results = gameList.objects.all().filter(gameName__contains=criteria).order_by(ordering)
        elif search == "genre":
            if criteria != "":
                results1 = gameDetails.objects.all().filter(genres__contains=criteria)
        elif search == "developer":
            if criteria != "":
                results1 = gameDetails.objects.all().filter(developer__contains=criteria)
        context = {
                "selected":selected,
                "criteria":criteria,
                "ordering":ordering,
                "asc_desc":asc_desc,
                "results":results,
                "results1":results1,
                "hide":hide,
                }
        return render(request, "search.html", context)

    context = {
                "selected":selected,
                "criteria":criteria,
                "ordering":ordering,
                "asc_desc":asc_desc,
                }
    return render(request, "search.html", context)


def cart(request):
    games = gameList.objects.filter(primaryGenre="Education")
    return render(request, "cart.html", {'games' : games})


def stats(request):
    #Bar Chart Data Code
    games = gameDetails.objects.all()
    score5_0 = 0
    score4_5 = 0
    score4_0 = 0
    score3_5 = 0
    score3_0 = 0
    score2_5 = 0
    score2_0 = 0
    score1_5 = 0
    score1_0 = 0

    for G in games:
        if G.averageUserRating == "5.0":
            score5_0 += 1
        elif G.averageUserRating == "4.5":
            score4_5 += 1
        elif G.averageUserRating == "4.0":
            score4_0 += 1
        elif G.averageUserRating == "3.5":
            score3_5 += 1
        elif G.averageUserRating == "3.0":
            score3_0 += 1
        elif G.averageUserRating == "2.5":
            score2_5 += 1
        elif G.averageUserRating == "2.0":
            score2_0 += 1
        elif G.averageUserRating == "1.5":
            score1_5 += 1
        elif G.averageUserRating == "1.0":
            score1_0 += 1
        else:
            print("ERROR")
    dataValues = [score5_0,score4_5,score4_0,score3_5,score3_0,score2_5,score2_0,score1_5,score1_0]

#Pie Chart Data Code
    genreList = []
    genreColourList = []
    genreCountList = []

    q = gameList.objects.values('primaryGenre').distinct()
    for x in q:
        for y in x.values():
            #print(y)
            genreList.append(str(y))
            genreCountList.append(gameList.objects.filter(primaryGenre=y).count())
            baseNo = gameList.objects.filter(primaryGenre=y).first()
            rNo = int((str(baseNo.gameID)[0])+(str(baseNo.gameID)[1])+(str(baseNo.gameID)[2]))%255
            gNo = int((str(baseNo.gameID)[3])+(str(baseNo.gameID)[4])+(str(baseNo.gameID)[5]))%255
            bNo = int((str(baseNo.gameID)[6])+(str(baseNo.gameID)[7])+(str(baseNo.gameID)[8]))%255
            genreColourList.append("rgba("+str(rNo)+","+str(gNo)+","+str(bNo)+")")

    
    #print(genreList)

#Scatter Graph Data Code
    XcoordinateList = []
    YcoordinateList = []
    scatterLabels = []
    a = 0
    b = 0
    c = ""
    lLength = 0
    games = gameDetails.objects.all()
    for m in games:
        a = m.numberOfRating
        b = m.gameID.price
        c = m.gameID.gameName
        #print("{x:"+str(b)+", y:"+str(a)+"}")
        YcoordinateList.append(a)
        XcoordinateList.append(b)
        scatterLabels.append(c)
        lLength += 1

    context = { "dataValues":dataValues,
                "genreList":genreList,
                "genreCountList":genreCountList,
                "genreColourList":genreColourList,
                "XcoordinateList":XcoordinateList,
                "YcoordinateList":YcoordinateList,
                "scatterLabels":scatterLabels,
                "lLength":lLength,
    }
    return render(request, "stats.html", context)
