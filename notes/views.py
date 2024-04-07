
from django.shortcuts import render
from .models import Notes
# Create your views here.

def create_notes(request):
    return render(request,'create-notes.html')


def create_notes(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        owner = request.user.id
        Notes.objects.create(title=title,content=content,owner=owner)
        # return redirect('homePage')

    return render(request,'create-notes.html')

def view_notes(request, id):
    notes_details = Notes.objects.get(id=id)
    
    context = {
        'notes': notes_details,
    }

    return render(request, 'view-notes.html', context)

def view_flashcards(request,id):
    return render(request, 'view-flashcards.html')