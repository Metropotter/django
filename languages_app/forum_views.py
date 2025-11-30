from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Question, Answer, Comment

def forum_home(request):
    questions = Question.objects.all()
    return render(request, 'languages_app/forum_home.html', {'questions': questions})

@login_required
def ask_question(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        tags = request.POST.get('tags', '')
        
        question = Question.objects.create(
            user=request.user,
            title=title,
            content=content,
            tags=tags
        )
        messages.success(request, 'Your question has been posted!')
        return redirect('languages_app:question_detail', question_id=question.id) 
    
    return render(request, 'languages_app/ask_question.html')

def question_detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'languages_app/question_detail.html', {'question': question})

@login_required
def add_comment(request, question_id):
    if request.method == 'POST':
        question = get_object_or_404(Question, id=question_id)
        content = request.POST['content']
        
        Comment.objects.create(
            question=question,
            user=request.user,
            content=content
        )
        messages.success(request, 'Comment added!')
    
    return redirect('languages_app:question_detail', question_id=question_id)