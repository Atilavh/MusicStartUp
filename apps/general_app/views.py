from django.shortcuts import render

# Create your views here.

# region IndexView
def index_view(request):
    context = {}
    return render(request, 'home-page/index.html', context)
# endregion