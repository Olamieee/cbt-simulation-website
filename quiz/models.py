from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to User model
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class OralQuestion(models.Model):
    question_text = models.TextField()
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=1)

    def __str__(self):
        return self.question_text

class ReadingComprehensionPassage(models.Model):
    passage_text = models.TextField()  # Stores the passage content

    def __str__(self):
        return f"Passage {self.id}"  # Display passage ID or first few words

class ReadingComprehensionQuestion(models.Model):
    passage = models.ForeignKey(ReadingComprehensionPassage, on_delete=models.CASCADE, related_name="questions")
    question_text = models.TextField()
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=1)

    def __str__(self):
        return f"Question {self.id} for Passage {self.passage.id}"

class QuizAttempt(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    quiz_type = models.CharField(max_length=50)
    score = models.IntegerField()
    total_questions = models.IntegerField()  # Make sure this exists
    date_taken = models.DateTimeField(default=timezone.now)  # Ensure this field exists

    def __str__(self):
        return f'{self.user.name} - {self.quiz_type}'

class Testimonial(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.user.username}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name