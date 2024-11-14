# WASSCE CBT Simulation Overview
A web platform designed to simulate the West African Senior School Certificate Examination (WASSCE) using advanced Computer-Based Test (CBT) technology. The project is aimed at providing students with a real-time exam environment to practice, gain familiarity with the exam format, and reduce exam anxiety.

Features</strong><br>
Timed Mock Exams: Simulate real WASSCE exams with timed tests for both Oral English and Reading Comprehension. <br>
User-Friendly Interface: Easy navigation and interactive design to enhance the user experience.<br>
Instant Feedback: Get feedback after each test to identify strengths and areas for improvement.<br>
Research-Based Design: Developed with guidance from Dr. Faloye Bankole Olagunju, this platform is backed by institutional research.


<strong>Technologies Used</strong><br>
1. Django: Backend framework for building the web application.<br>
2. HTML/CSS: For structuring and styling the web pages.<br>
3. JavaScript: For any interactive features on the frontend<br>.
4. PostgreSQL: Database for storing user information, tests, and feedback.

<strong>Installation</strong><br>
Prerequisites
Python 3.x
PostgreSQL (or your preferred database)
Django 5.1.1
Required libraries in requirements.txt

Steps to Install Locally
Clone the repository:

bash
Copy code
git clone https://github.com/YourUsername/cbt_simulation.git
cd cbt_simulation
Set up a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use 'venv\Scripts\activate'
Install the dependencies:

bash
pip install -r requirements.txt
Set up your PostgreSQL database:

Create a new PostgreSQL database.

Update the database settings in settings.py:

python

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
<br>
Run migrations to set up your database: <br>

bash
python manage.py migrate
<br>

Create a superuser to access the Django admin:
bash
python manage.py createsuperuser
<br>

Start the development server:
bash
python manage.py runserver

Visit http://127.0.0.1:8000/ in your browser to see the site in action.

<strong>Usage</strong><br>
Once the platform is running, users can:<br>
Take a CBT Simulation by selecting from available tests.<br>
Practice Oral English and Reading Comprehension under timed conditions.<br>
Submit feedback or view test results after completion.<br>

<strong>Contributing</strong><br>
If you'd like to contribute to this project, please fork the repository, create a new branch for your feature, and submit a pull request with your changes.

<strong>Authors</strong><br>
Dr. Faloye Bankole Olagunju (PhD) - Principal Investigator<br>
Alonge Olamide Samson - Project Lead and Developer | alongeola16@gmail.com
