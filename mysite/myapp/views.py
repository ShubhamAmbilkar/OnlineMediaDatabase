from django.shortcuts import render, render_to_response
from .forms import MediaForm
from .models import Media
# Create your views here.
def index(request):
    return render_to_response('index.html')

def abstracter(request):
    return render(request , 'abstraction.html')

def action_movies(request):
    title = "Action Movies"
    actmvs = Media.objects.filter(genre="Action")
    tem = actmvs.order_by('-ratings')
    return render(request,'abs_view.html',{'title':title , 'mvs':tem})


def thriller_movies(request):
    title = "Thriller Movies"
    trlmvs = Media.objects.filter(genre="Thriller")
    rem = trlmvs.order_by('-ratings')
    return render(request, 'abs_view.html',{'title':title , 'mvs':rem})

def best_movies(request):
    title = "Best Movies"
    trlmvs = Media.objects.order_by('-ratings')
    return render(request, 'abs_view.html', {'title': title, 'mvs': trlmvs})

def raid(request):
    return render(request , 'new2.html')

def movie_form(request):
    if request.method == "POST":
        form = MediaForm(request.POST)
        if form.is_valid():
            form.save(commit=True)

            return render(request , 'index.html')
    else:
        form = MediaForm()
    return render(request, 'movie_form.html', {'form':form})