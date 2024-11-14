"""
URL configuration for cbt_simulation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from quiz import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('oral-quiz/', views.take_oral_quiz, name='oral_quiz'),
    path('reading-comprehension-quiz/', views.reading_comprehension_quiz, name='reading_comprehension_quiz'),
    path('submit_answers/', views.submit_answers, name='submit_answers'),
    # path('import-oral-questions/', views.oral_question_import_from_text, name='oral_question_import_from_text'),
    # path('upload_reading_comprehension/', views.upload_reading_comprehension, name='upload_reading_comprehension'),  # Upload page 
    path('contact/', views.contact_us, name='contact'),
    path('about/', views.about, name='about'),
    path('cbt-simulation/', views.cbt_simulation, name='cbt_simulation'),  # New path for CBT Simulation intro page
    path("submit-review/", views.submit_review, name="submit_review"),
    path('submit-review-homepage/', views.submit_review_from_homepage, name='submit_review_homepage'),
]
