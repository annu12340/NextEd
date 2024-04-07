
from django.shortcuts import render

# Create your views here.

def create_notes(request):
    return render(request,'create-notes.html')


def create_notes(request):
    return render(request,'create-notes.html')

def view_notes(request, id):
    notes_details = Notes.objects.get(id=id)
    context = {
        'notes': notes_details,
    }

    return render(request, 'user/doctor-details.html', context)