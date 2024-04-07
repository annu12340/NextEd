
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

def quiz(request,id):
    questions = [
        "1What distinguishes crystalline solids from amorphous solids, and how do their internal structures differ?",
        "2Describe the bonding and properties of ionic solids, using examples such as sodium chloride and nickel oxide to illustrate.",
        "3Explain the physical properties of crystalline solids that are primarily determined by the forces holding their particles together."
    ]
    total_score = 0
    feedback = ""

    if request.method == "POST":
        current_question_index = int(request.POST.get('current_question_index', 0))
        user_answer = request.POST.get('answer', '')
        
        # Assuming you have a function to calculate score and feedback based on answers
        total_score, feedback = calculate_score_and_feedback(user_answer, questions[current_question_index])
        
        if current_question_index < len(questions) - 1:
            current_question_index += 1

    else:
        current_question_index = 0

    current_question = questions[current_question_index]

    return render(request, 'quiz.html', {
        'current_question': current_question,
        'total_score': total_score,
        'feedback': feedback,
        'current_question_index': current_question_index,
        'questions_count': len(questions)
    })



def calculate_score_and_feedback(user_answer, correct_answer):
    # Calculate total score based on answers
    # Determine feedback based on answers
    total_score=0
    feedback=''
    return total_score, feedback