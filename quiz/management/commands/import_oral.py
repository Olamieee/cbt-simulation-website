import re
from django.core.management.base import BaseCommand
from quiz.models import OralQuestion

class Command(BaseCommand):
    help = 'Imports oral questions from a text file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='The path to the text file containing oral questions')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Regular expression pattern to match each question block
        question_pattern = re.compile(
            r"\d+\.\s*(.*?)\s*A\.\s(.*?)\s*B\.\s(.*?)\s*C\.\s(.*?)\s*D\.\s(.*?)\s*Correct Answer:\s([A-D])",
            re.MULTILINE | re.DOTALL
        )

        for match in question_pattern.finditer(content):
            question_text = match.group(1).strip()
            option_a = match.group(2).strip()
            option_b = match.group(3).strip()
            option_c = match.group(4).strip()
            option_d = match.group(5).strip()
            correct_answer = match.group(6).strip()

            # Create an OralQuestion entry
            OralQuestion.objects.create(
                question_text=question_text,
                option_a=option_a,
                option_b=option_b,
                option_c=option_c,
                option_d=option_d,
                correct_answer=correct_answer
            )

        self.stdout.write(self.style.SUCCESS('Successfully imported oral questions'))
