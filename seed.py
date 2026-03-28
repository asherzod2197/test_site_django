"""
Seed script — creates admin user, sample categories, quizzes, and parses markdown files.
Run:  .venv\Scripts\python seed.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User
from quiz.models import Category, Quiz, Question
from quiz.md_parser import parse_quiz_markdown
from django.conf import settings


def seed():
    print('Seeding database...')

    # --- Admin user ---
    if not User.objects.filter(username='admin').exists():
        admin = User.objects.create_superuser(
            username='admin',
            password='admin123',
            email='admin@quizhub.local'
        )
        print(f'  Admin yaratildi: admin / admin123')
    else:
        print('  Admin allaqachon mavjud.')

    # --- Categories ---
    categories_data = [
        {'name': 'Python', 'slug': 'python', 'description': 'Python dasturlash tili bo\'yicha testlar'},
        {'name': 'JavaScript', 'slug': 'javascript', 'description': 'JavaScript dasturlash tili bo\'yicha testlar'},
        {'name': 'SQL', 'slug': 'sql', 'description': 'SQL ma\'lumotlar bazasi bo\'yicha testlar'},
        {'name': 'HTML/CSS', 'slug': 'html-css', 'description': 'Web frontend asoslari bo\'yicha testlar'},
    ]

    cat_map = {}
    for c_data in categories_data:
        cat, created = Category.objects.get_or_create(
            slug=c_data['slug'],
            defaults={'name': c_data['name'], 'description': c_data['description']}
        )
        cat_map[c_data['slug']] = cat
        status = 'yaratildi' if created else 'mavjud'
        print(f'  Kategoriya: {cat.name} — {status}')

    # --- Quizzes from MD files ---
    quizzes_data = [
        {
            'title': 'Python Asoslari',
            'description': 'Python dasturlash tilining asosiy tushunchalari: o\'zgaruvchilar, funksiyalar, ro\'yxatlar, lug\'atlar va boshqalar.',
            'md_file': 'python_basics.md',
            'category_slug': 'python',
            'difficulty': 'easy',
        },
        {
            'title': 'JavaScript Asoslari',
            'description': 'JavaScript tilining asosiy tushunchalari: typeof, equality, massivlar, asinxronlik va destructuring.',
            'md_file': 'javascript.md',
            'category_slug': 'javascript',
            'difficulty': 'medium',
        },
    ]

    for q_data in quizzes_data:
        # Check if quiz already exists
        if Quiz.objects.filter(title=q_data['title']).exists():
            print(f'  Test allaqachon mavjud: {q_data["title"]}')
            continue

        # Read markdown file
        md_path = os.path.join(settings.QUIZZES_DIR, q_data['md_file'])
        if not os.path.exists(md_path):
            print(f'  XATO: MD fayl topilmadi: {md_path}')
            continue

        with open(md_path, 'r', encoding='utf-8') as f:
            md_content = f.read()

        # Create quiz
        quiz = Quiz.objects.create(
            title=q_data['title'],
            description=q_data['description'],
            markdown_file=q_data['md_file'],
            category=cat_map[q_data['category_slug']],
            difficulty=q_data['difficulty'],
        )

        # Parse and create questions
        questions = parse_quiz_markdown(md_content)
        for q in questions:
            Question.objects.create(quiz=quiz, **q)

        print(f'  Test yaratildi: {quiz.title} ({len(questions)} savol)')

    print('\nSeeding tugadi!')
    print(f'  Kategoriyalar: {Category.objects.count()}')
    print(f'  Testlar: {Quiz.objects.count()}')
    print(f'  Savollar: {Question.objects.count()}')
    print(f'  Admin: admin / admin123')


if __name__ == '__main__':
    seed()
