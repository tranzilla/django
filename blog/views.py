from django.shortcuts import render

# Create your views here - Logic of the application - Controller
def post_list(request):
    return render(request, 'blog/post_list.html', {})
