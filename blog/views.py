from django.shortcuts import render

def publication_list(request):
    return render(request, 'blog/publication_list.html', {})
