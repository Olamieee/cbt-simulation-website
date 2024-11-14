from django.shortcuts import render, redirect, get_object_or_404
from .models import OralQuestion, ReadingComprehensionQuestion, UserProfile, QuizAttempt, Testimonial, ReadingComprehensionPassage
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import ContactForm
import random
import re 
from django.contrib.auth.models import User

# Homepage
def home(request):
    # Check if user is registered (exists in session)
    if 'user_id' not in request.session:
        return redirect('register')  # Redirect to registration page if not registered
    testimonials = Testimonial.objects.all()  # Limit to recent 5 testimonials
    return render(request, 'home.html', {'testimonials': testimonials})

# Regisration Page
def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']

        # Create User instance with just a username and email (username can be the same as email)
        user = User.objects.create_user(username=email, email=email)
        user.save()

        # Now create UserProfile instance linked to this User
        user_profile = UserProfile.objects.create(user=user, name=name, email=email)
        
        # Store user profile ID in session
        request.session['user_id'] = user_profile.id
        return redirect('home')
    return render(request, 'register.html')

# Oral Test page
def take_oral_quiz(request):
    # Ensure user is registered before starting quiz
    if 'user_id' not in request.session:
        return redirect('register')  # Redirect to registration page if not registered

    # Fetch and shuffle questions for the quiz
    questions = list(OralQuestion.objects.all())
    random.shuffle(questions)
    selected_questions = questions[:30]  # Pick 10 random questions

    if request.method == 'POST':
        score = 0
        total_questions = len(selected_questions)
        for question in selected_questions:
            user_answer = request.POST.get(f'question_{question.id}')
            if user_answer == question.correct_answer:
                score += 1

        # Save the quiz attempt for the user
        user = UserProfile.objects.get(id=request.session['user_id'])
        QuizAttempt.objects.create(user=user, quiz_type='Oral Quiz', score=score, total_questions=total_questions)

        # Personalize the result page
        return render(request, 'quiz_result.html', {
            'name': user.name,
            'score': score,
            'total_questions': total_questions,
            'quiz_type': 'oral',
        })

    # Pass selected questions and time limit to the quiz template
    time_limit_in_seconds = 30 * 60  # Example: 30 minutes * 60 seconds
    return render(request, 'quiz_navigation.html', {
        'questions': selected_questions,
        'quiz_name': 'Oral Quiz',
        'time_limit_in_seconds': time_limit_in_seconds
    })

# Reading Comprehsnion Test page
def reading_comprehension_quiz(request):
    if 'user_id' not in request.session:
        return redirect('register')

    # Select 5 random passages
    passages = list(ReadingComprehensionPassage.objects.all())
    selected_passages = random.sample(passages, min(len(passages), 5))  # Fetch 5 or fewer if not available

    # Retrieve questions for each selected passage
    passages_with_questions = []
    for passage in selected_passages:
        questions = list(ReadingComprehensionQuestion.objects.filter(passage=passage).select_related('passage'))
        print(f"Passage ID {passage.id} - Questions: {[q.question_text for q in questions]}")  # Debug print

        passages_with_questions.append({
            'passage': passage,
            'questions': questions
        })

    if request.method == 'POST':
        score = 0
        total_questions = sum(len(pwq['questions']) for pwq in passages_with_questions)

        # Grade each question
        for pwq in passages_with_questions:
            for question in pwq['questions']:
                user_answer = request.POST.get(f'question_{question.id}')
                if user_answer == question.correct_answer:
                    score += 1

        # Record the quiz attempt
        user = UserProfile.objects.get(id=request.session['user_id'])
        QuizAttempt.objects.create(
            user=user, quiz_type='Reading Comprehension Quiz', score=score, total_questions=total_questions
        )

        return render(request, 'quiz_result.html', {
            'name': user.name,
            'score': score,
            'total_questions': total_questions,
            'quiz_type': 'passage'
        })

    time_limit_in_seconds = 45 * 60
    return render(request, 'reading_comprehension_quiz.html', {
        'passages_with_questions': passages_with_questions,
        'quiz_name': 'Reading Comprehension Quiz',
        'time_limit_in_seconds': time_limit_in_seconds
    })


def submit_answers(request):
    if request.method == 'POST':
        score = 0
        total_questions = 0
        for question_id, selected_option in request.POST.items():
            if question_id.startswith('question_'):
                question_id = question_id.split('_')[1]
                question = OralQuestion.objects.get(id=question_id)
                if question.correct_answer == selected_option:
                    score += 1
                total_questions += 1

        return JsonResponse({
            'score': score,
            'total_questions': total_questions
        })

# def oral_question_import_from_text(request):
#     if request.method == 'POST' and 'text_file' in request.FILES:
#         text_file = request.FILES['text_file']
#         content = text_file.read().decode('utf-8').splitlines()

#         question_pattern = re.compile(r'^\d+\. (.+?)$')
#         option_pattern = re.compile(r'^[A-D]\. (.+)$')
#         answer_pattern = re.compile(r'^Correct Answer: ([A-D])$')

#         question_text, options, correct_answer = '', [], ''
#         for line in content:
#             q_match = question_pattern.match(line)
#             o_match = option_pattern.match(line)
#             a_match = answer_pattern.match(line)

#             if q_match:
#                 question_text = q_match.group(1)
#                 options = []
#             elif o_match:
#                 options.append(o_match.group(1))
#             elif a_match:
#                 correct_answer = a_match.group(1)

#                 # Save the question to the database once fully parsed
#                 try:
#                     if len(options) == 4:
#                         OralQuestion.objects.create(
#                             question_text=question_text,
#                             option_a=options[0],
#                             option_b=options[1],
#                             option_c=options[2],
#                             option_d=options[3],
#                             correct_answer=correct_answer
#                         )
#                         print("Saved question:", question_text)
#                     else:
#                         print("Skipping question due to incomplete options:", question_text)
#                 except Exception as e:
#                     print("Error saving question:", question_text, e)

#         return redirect('oral_quiz')  # Redirect to a page listing questions

#     return render(request, 'import_questions.html')


def cbt_simulation(request):
    return render(request, 'cbt_simulation.html')

# Contact page
def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # This saves the form data to the database
            return redirect('contact')  # Redirect to a success page or back to the contact page
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


# About page
def about(request):
    return render(request, 'about.html')

# Review page
def submit_review(request):
    if request.method == 'POST':
        review_text = request.POST.get('review')
        user_id = request.session.get('user_id')  # Retrieve user ID from session

        # Check if user profile exists
        try:
            user_profile = UserProfile.objects.get(id=user_id)
        except UserProfile.DoesNotExist:
            return HttpResponse("User profile not found", status=404)

        # Save the review
        Testimonial.objects.create(user=user_profile, review=review_text)

        # Redirect to the home page or quiz results page after submission
        return redirect('home')

    # If not a POST request, redirect back to the homepage
    return redirect('home')

def submit_review_from_homepage(request):
    if request.method == 'POST':
        review_text = request.POST.get('review')
        user_id = request.session.get('user_id')  # Assuming user_id is stored in session

        try:
            user_profile = UserProfile.objects.get(id=user_id)
        except UserProfile.DoesNotExist:
            return HttpResponse("User profile not found", status=404)

        Testimonial.objects.create(user=user_profile, review=review_text)
        return redirect('home')

    return render(request, 'submit_review_home.html')