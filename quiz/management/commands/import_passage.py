import re
from django.core.management.base import BaseCommand
from quiz.models import ReadingComprehensionPassage, ReadingComprehensionQuestion

class Command(BaseCommand):
    help = 'Imports reading comprehension passages and questions from a text file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='The path to the text file containing passages and questions')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"File not found: {file_path}"))
            return
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error reading file: {e}"))
            return

        # Split content by each passage
        passages = re.split(r'Passage \d+:', content)[1:]

        for passage_text in passages:
            lines = passage_text.strip().split('\n')
            passage_content = ""
            questions = []

            # Separate passage text and questions
            for line in lines:
                if line.startswith("Questions:"):
                    break
                passage_content += line + " "

            try:
                # Create a Passage entry
                passage = ReadingComprehensionPassage.objects.create(passage_text=passage_content.strip())
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Error creating passage: {e}"))
                continue

            # Extract questions and answers
            question_pattern = re.compile(
                r"^(.*\?)\s*A\.\s(.*)\s*B\.\s(.*)\s*C\.\s(.*)\s*D\.\s(.*)\s*Correct Answer:\s([A-D])",
                re.MULTILINE
            )
            questions_text = "\n".join(lines[len(passage_content.splitlines()) + 1:])

            for match in question_pattern.finditer(questions_text):
                question_text = match.group(1).strip()
                option_a = match.group(2).strip()
                option_b = match.group(3).strip()
                option_c = match.group(4).strip()
                option_d = match.group(5).strip()
                correct_answer = match.group(6).strip()

                try:
                    # Create Question entry linked to the passage
                    ReadingComprehensionQuestion.objects.create(
                        passage=passage,  # Linking to the Passage instance
                        question_text=question_text,
                        option_a=option_a,
                        option_b=option_b,
                        option_c=option_c,
                        option_d=option_d,
                        correct_answer=correct_answer
                    )
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Error creating question for passage {passage.id}: {e}"))

        self.stdout.write(self.style.SUCCESS('Successfully imported passages and questions'))
