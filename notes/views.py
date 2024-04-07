
from django.shortcuts import render
from .models import Notes
# Create your views here.
from openai import OpenAI

YOUR_API_KEY = "INSERT API KEY HERE"

def create_notes(request):
    return render(request,'create-notes.html')


def create_notes(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        owner = request.user.id
        
        short_notes=openai_response(f"Summarize the text into short and crisp notes {content}")
        questions=openai_response(f"Create questions and answers for this content {content}")
        mnemonics=openai_response(f"Create a mnemonics for this text {content}")
        simple_explanation=openai_response(f"Imagine that you are my mentor. Explain this topic like I am 5 {content}")
        Notes.objects.create(title=title,content=short_notes,owner=owner,mnemonics=mnemonics,questions=questions,simple_explanation=simple_explanation)
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


def openai_response(prompt):

    messages = [
    
        {
            "role": "user",
            "content": (
            prompt
            ),
        },
    ]

    client = OpenAI(api_key=YOUR_API_KEY, base_url="https://api.perplexity.ai")


    # chat completion with streaming
    response_stream = client.chat.completions.create(
        model="mistral-7b-instruct",
        messages=messages,
        stream=True,
    )
    result=''
    for response in response_stream:
        result+=response
    return response


def calculate_score_and_feedback(user_answer, correct_answer):
    # Calculate total score based on answers
    # Determine feedback based on answers
    total_score=0
    feedback=''
    return total_score, feedback