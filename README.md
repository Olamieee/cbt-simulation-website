
# WASSCE CBT Simulation

## Overview

The **WASSCE CBT Simulation** is a web platform designed to simulate the West African Senior School Certificate Examination (WASSCE) using advanced Computer-Based Test (CBT) technology. This project aims to provide students with a real-time exam environment to practice, gain familiarity with the exam format, and reduce exam anxiety.

## Features

- **Timed Mock Exams**: Simulate real WASSCE exams with timed tests for both **Oral English** and **Reading Comprehension**.
- **User-Friendly Interface**: Easy navigation and interactive design to enhance the user experience.
- **Instant Feedback**: Get feedback after each test to identify strengths and areas for improvement.
- **Research-Based Design**: Developed with guidance from **Dr. Faloye Bankole Olagunju** (PhD), this platform is backed by institutional research.

## Technologies Used

1. **Django**: Backend framework for building the web application.
2. **HTML/CSS**: For structuring and styling the web pages.
3. **JavaScript**: For any interactive features on the frontend.
4. **PostgreSQL**: Database for storing user information, tests, and feedback.

## Installation

### Prerequisites

- **Python 3.x**
- **PostgreSQL** (or your preferred database)
- **Django**
- Required libraries (listed in `requirements.txt`)

### Steps to Install Locally

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Olamieee/cbt-simulation-website.git
   cd cbt_simulation
   ```

2. **Set up a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use 'venv\Scriptsctivate'
   ```

3. **Install the dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your PostgreSQL database**:

   - Create a new PostgreSQL database.
   - Update the `DATABASES` configuration in `settings.py`:

     ```python
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
     ```

5. **Run migrations** to set up your database:

   ```bash
   python manage.py migrate
   ```

6. **Create a superuser** to access the Django admin:

   ```bash
   python manage.py createsuperuser
   ```

7. **Start the development server**:

   ```bash
   python manage.py runserver
   ```

8. **Visit** `http://127.0.0.1:8000/` in your browser to see the site in action.

## Usage

Once the platform is running, users can:

- Take a **CBT Simulation** by selecting from available tests.
- Practice **Oral English** and **Reading Comprehension** under timed conditions.
- Submit feedback or view test results after completion.

## Contributing

If you'd like to contribute to this project, please:

1. **Fork** the repository.
2. **Create a new branch** for your feature.
3. **Submit a pull request** with your changes.

## Authors

- **Dr. Faloye Bankole Olagunju** (PhD) - Principal Investigator
- **Alonge Olamide Samson** - Project Lead and Developer  
  Email: [alongeola16@gmail.com](mailto:alongeola16@gmail.com)
