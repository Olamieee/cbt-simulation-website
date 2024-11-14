from django.contrib import admin
from .models import OralQuestion, ReadingComprehensionPassage, ReadingComprehensionQuestion, UserProfile, QuizAttempt, Testimonial, ContactMessage

# Register the OralQuestion model
@admin.register(OralQuestion)
class OralQuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'option_a', 'option_b', 'option_c', 'option_d', 'correct_answer')

# Register the ReadingComprehensionPassage model
@admin.register(ReadingComprehensionPassage)
class ReadingComprehensionPassageAdmin(admin.ModelAdmin):
    list_display = ('id', 'passage_text')

# Register the ReadingComprehensionQuestion model
@admin.register(ReadingComprehensionQuestion)
class ReadingComprehensionQuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'option_a', 'option_b', 'option_c', 'option_d', 'correct_answer', 'passage')
    list_filter = ('passage',)

@admin.register(QuizAttempt)
class QuizAttemptAdmin(admin.ModelAdmin):
    list_display = ('user', 'quiz_type', 'score', 'total_questions', 'date_taken')  # Ensure these fields exist in the model

admin.site.register(UserProfile)

admin.site.register(Testimonial)


admin.site.register(ContactMessage)