import os
import random
import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.http import JsonResponse
from django.conf import settings
from django.utils import timezone
from django.views.decorators.http import require_POST

from .models import Category, Quiz, Question, UserResult
from .forms import LoginForm, RegisterForm, QuizForm, CategoryForm
from .md_parser import parse_quiz_markdown, render_markdown, render_inline_markdown
from datetime import datetime


# ---------------------------------------------------------------------------
# Public views
# ---------------------------------------------------------------------------

def _get_completed_quiz_ids(user):
    """Return set of quiz IDs that the user has already completed."""
    if user.is_authenticated:
        return set(UserResult.objects.filter(user=user).values_list('quiz_id', flat=True))
    return set()


def index(request):
    """Home page — quiz list with category filter and pagination."""
    quizzes = Quiz.objects.select_related('category').annotate(
        q_count=Count('questions')
    )
    category_slug = request.GET.get('category')
    if category_slug:
        quizzes = quizzes.filter(category__slug=category_slug)

    difficulty = request.GET.get('difficulty')
    if difficulty:
        quizzes = quizzes.filter(difficulty=difficulty)

    paginator = Paginator(quizzes, 10)
    page = request.GET.get('page')
    quizzes_page = paginator.get_page(page)
    return render(request, 'index.html', {
        'quizzes': quizzes_page,
        'current_category': category_slug,
        'current_difficulty': difficulty,
        'completed_quiz_ids': _get_completed_quiz_ids(request.user),
        'stat_quizzes': Quiz.objects.count(),
        'stat_questions': Question.objects.count(),
        'stat_users': User.objects.count(),
        'stat_results': UserResult.objects.count(),
    })


@login_required
def quiz_detail(request, quiz_id):
    """Quiz detail — show all questions for taking the quiz."""
    quiz = get_object_or_404(Quiz, id=quiz_id)

    # Check if user already completed this quiz — redirect to saved result
    if request.user.is_authenticated:
        existing_result = UserResult.objects.filter(user=request.user, quiz=quiz).first()
        if existing_result:
            messages.info(request, 'Siz bu testni allaqachon topshirgansiz. Qayta topshirish mumkin emas.')
            return redirect('quiz_result', quiz_id=quiz.id)

    questions = list(quiz.questions.all())
    random.shuffle(questions)  # Randomize question order

    # Render markdown for each question with shuffled options
    questions_data = []
    for q in questions:
        # Build options list with original letter keys
        options = [
            ('a', q.option_a),
            ('b', q.option_b),
            ('c', q.option_c),
            ('d', q.option_d),
        ]
        # Remove empty options
        options = [(k, v) for k, v in options if v]
        # Shuffle option order
        random.shuffle(options)

        questions_data.append({
            'id': q.id,
            'question_html': render_markdown(q.question_md),
            'options': [{'value': k, 'text': render_inline_markdown(v)} for k, v in options],
            'correct_option': q.correct_option,
            'explanation_html': render_markdown(q.explanation_md),
            'order_index': q.order_index,
        })

    return render(request, 'quiz_detail.html', {
        'quiz': quiz,
        'questions_json': json.dumps(questions_data, ensure_ascii=False),
        'question_count': len(questions_data),
        'start_time': timezone.now().isoformat(),
    })


@require_POST
def quiz_submit(request, quiz_id):
    """Submit quiz answers and save result."""
    quiz = get_object_or_404(Quiz, id=quiz_id)

    # Block double submission for authenticated users
    if request.user.is_authenticated:
        if UserResult.objects.filter(user=request.user, quiz=quiz).exists():
            messages.warning(request, 'Siz bu testni allaqachon topshirgansiz.')
            return redirect('quiz_result', quiz_id=quiz.id)

    questions = quiz.questions.all()

    score = 0
    total = questions.count()
    answers = {}

    for q in questions:
        user_answer = request.POST.get(f'question_{q.id}', '').lower()
        answers[str(q.id)] = user_answer
        if user_answer == q.correct_option:
            score += 1

    # Save result if user is authenticated
    if request.user.is_authenticated:
        # Parse start_time from hidden field
        start_time_str = request.POST.get('start_time', '')
        started_at = None
        if start_time_str:
            try:
                started_at = datetime.fromisoformat(start_time_str)
            except (ValueError, TypeError):
                started_at = None

        UserResult.objects.create(
            user=request.user,
            quiz=quiz,
            score=score,
            total=total,
            started_at=started_at,
        )

    # Prepare detailed results
    results = []
    for q in questions:
        user_answer = answers.get(str(q.id), '')
        results.append({
            'question_html': render_markdown(q.question_md),
            'option_a': render_inline_markdown(q.option_a),
            'option_b': render_inline_markdown(q.option_b),
            'option_c': render_inline_markdown(q.option_c),
            'option_d': render_inline_markdown(q.option_d),
            'correct_option': q.correct_option,
            'user_answer': user_answer,
            'is_correct': user_answer == q.correct_option,
            'explanation_html': render_markdown(q.explanation_md),
        })

    percentage = round(score / total * 100) if total > 0 else 0

    return render(request, 'result.html', {
        'quiz': quiz,
        'score': score,
        'total': total,
        'percentage': percentage,
        'results': results,
    })


def category_page(request, slug):
    """Category page — quizzes filtered by category."""
    category = get_object_or_404(Category, slug=slug)
    quizzes = Quiz.objects.filter(category=category).annotate(
        q_count=Count('questions')
    )
    paginator = Paginator(quizzes, 10)
    page = request.GET.get('page')
    quizzes_page = paginator.get_page(page)
    return render(request, 'category.html', {
        'category': category,
        'quizzes': quizzes_page,
        'completed_quiz_ids': _get_completed_quiz_ids(request.user),
    })


def search(request):
    """Search quizzes by title or category name."""
    q = request.GET.get('q', '').strip()
    quizzes = Quiz.objects.annotate(q_count=Count('questions'))
    if q:
        quizzes = quizzes.filter(
            Q(title__icontains=q) | Q(category__name__icontains=q) | Q(description__icontains=q)
        )
    paginator = Paginator(quizzes, 10)
    page = request.GET.get('page')
    quizzes_page = paginator.get_page(page)
    return render(request, 'search.html', {
        'quizzes': quizzes_page,
        'query': q,
        'completed_quiz_ids': _get_completed_quiz_ids(request.user),
    })


@login_required
def quiz_result(request, quiz_id):
    """View saved quiz result (for quizzes already taken)."""
    quiz = get_object_or_404(Quiz, id=quiz_id)
    result = get_object_or_404(UserResult, user=request.user, quiz=quiz)
    questions = quiz.questions.all()

    percentage = result.percentage()

    # We don't have saved individual answers, so show summary only
    results = []
    for q in questions:
        results.append({
            'question_html': render_markdown(q.question_md),
            'option_a': render_inline_markdown(q.option_a),
            'option_b': render_inline_markdown(q.option_b),
            'option_c': render_inline_markdown(q.option_c),
            'option_d': render_inline_markdown(q.option_d),
            'correct_option': q.correct_option,
            'explanation_html': render_markdown(q.explanation_md),
        })

    return render(request, 'result_saved.html', {
        'quiz': quiz,
        'result': result,
        'score': result.score,
        'total': result.total,
        'percentage': percentage,
        'results': results,
    })


@login_required
def profile(request):
    """User profile — quiz results history."""
    results = UserResult.objects.filter(user=request.user).select_related('quiz', 'quiz__category')
    return render(request, 'profile.html', {'results': results})


# ---------------------------------------------------------------------------
# Auth views
# ---------------------------------------------------------------------------

def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, 'Tizimga muvaffaqiyatli kirdingiz!')
            next_url = request.GET.get('next', 'index')
            return redirect(next_url)
        else:
            messages.error(request, "Noto'g'ri foydalanuvchi nomi yoki parol.")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def register_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Ro'yxatdan muvaffaqiyatli o'tdingiz!")
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, 'Tizimdan chiqdingiz.')
    return redirect('index')


# ---------------------------------------------------------------------------
# Admin views
# ---------------------------------------------------------------------------

def is_admin(user):
    return user.is_staff or user.is_superuser


def admin_required(view_func):
    """Decorator: login required + admin (is_staff) required."""
    @login_required
    def wrapper(request, *args, **kwargs):
        if not is_admin(request.user):
            messages.error(request, 'Sizda admin huquqlari yo\'q.')
            return redirect('index')
        return view_func(request, *args, **kwargs)
    wrapper.__name__ = view_func.__name__
    return wrapper


@admin_required
def admin_dashboard(request):
    return render(request, 'admin/dashboard.html', {
        'quiz_count': Quiz.objects.count(),
        'question_count': Question.objects.count(),
        'category_count': Category.objects.count(),
        'user_count': User.objects.count(),
        'recent_results': UserResult.objects.select_related('user', 'quiz')[:10],
    })


# ---- Quiz CRUD ----

@admin_required
def admin_quiz_list(request):
    quizzes = Quiz.objects.select_related('category').annotate(q_count=Count('questions'))
    paginator = Paginator(quizzes, 20)
    page = request.GET.get('page')
    quizzes_page = paginator.get_page(page)
    return render(request, 'admin/quiz_list.html', {'quizzes': quizzes_page})


@admin_required
def admin_quiz_add(request):
    if request.method == 'POST':
        form = QuizForm(request.POST, request.FILES)
        if form.is_valid():
            quiz = form.save()
            md_content = _get_markdown_content(request, form)
            if md_content:
                _save_md_and_parse(quiz, md_content)
                messages.success(request, f'Test "{quiz.title}" muvaffaqiyatli yaratildi! ({quiz.questions.count()} savol)')
            else:
                messages.warning(request, 'Test yaratildi, lekin savollar topilmadi. Markdown kontent qo\'shing.')
            return redirect('admin_quiz_list')
    else:
        form = QuizForm()
    return render(request, 'admin/quiz_form.html', {'form': form, 'editing': False})


@admin_required
def admin_quiz_edit(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    # Get existing markdown content
    existing_md = ''
    if quiz.markdown_file:
        md_path = os.path.join(settings.QUIZZES_DIR, quiz.markdown_file)
        if os.path.exists(md_path):
            with open(md_path, 'r', encoding='utf-8') as f:
                existing_md = f.read()

    if request.method == 'POST':
        form = QuizForm(request.POST, request.FILES, instance=quiz)
        if form.is_valid():
            quiz = form.save()
            md_content = _get_markdown_content(request, form)
            if md_content:
                quiz.questions.all().delete()
                _save_md_and_parse(quiz, md_content)
                messages.success(request, f'Test yangilandi! ({quiz.questions.count()} savol)')
            else:
                messages.success(request, 'Test yangilandi!')
            return redirect('admin_quiz_list')
    else:
        form = QuizForm(instance=quiz)
    return render(request, 'admin/quiz_form.html', {
        'form': form,
        'editing': True,
        'quiz': quiz,
        'existing_md': existing_md,
    })


@admin_required
@require_POST
def admin_quiz_delete(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    title = quiz.title
    # Delete md file
    if quiz.markdown_file:
        md_path = os.path.join(settings.QUIZZES_DIR, quiz.markdown_file)
        if os.path.exists(md_path):
            os.remove(md_path)
    quiz.delete()
    messages.info(request, f'Test "{title}" o\'chirildi.')
    return redirect('admin_quiz_list')


def _get_markdown_content(request, form):
    """Get markdown content from file upload or textarea."""
    md_file = request.FILES.get('markdown_upload')
    if md_file:
        return md_file.read().decode('utf-8')
    md_text = form.cleaned_data.get('markdown_content', '').strip()
    if md_text:
        return md_text
    return ''


def _save_md_and_parse(quiz, md_content):
    """Save markdown file and parse questions into database."""
    os.makedirs(settings.QUIZZES_DIR, exist_ok=True)
    filename = f'quiz_{quiz.id}.md'
    filepath = os.path.join(settings.QUIZZES_DIR, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(md_content)
    quiz.markdown_file = filename
    quiz.save()

    questions = parse_quiz_markdown(md_content)
    for q_data in questions:
        Question.objects.create(quiz=quiz, **q_data)


# ---- Category CRUD ----

@admin_required
def admin_category_list(request):
    categories = Category.objects.annotate(quiz_count=Count('quizzes'))
    return render(request, 'admin/category_list.html', {'categories': categories})


@admin_required
def admin_category_add(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Kategoriya yaratildi!')
            return redirect('admin_category_list')
    else:
        form = CategoryForm()
    return render(request, 'admin/category_form.html', {'form': form, 'editing': False})


@admin_required
def admin_category_edit(request, cat_id):
    category = get_object_or_404(Category, id=cat_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Kategoriya yangilandi!')
            return redirect('admin_category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'admin/category_form.html', {
        'form': form,
        'editing': True,
        'category': category,
    })


@admin_required
@require_POST
def admin_category_delete(request, cat_id):
    category = get_object_or_404(Category, id=cat_id)
    if category.quizzes.count() > 0:
        messages.error(request, "Kategoriyada testlar mavjud. Avval testlarni o'chiring.")
        return redirect('admin_category_list')
    category.delete()
    messages.info(request, "Kategoriya o'chirildi.")
    return redirect('admin_category_list')


# ---- Users list ----

@admin_required
def admin_user_list(request):
    users = User.objects.annotate(result_count=Count('results'))
    return render(request, 'admin/user_list.html', {'users': users})


# ---------------------------------------------------------------------------
# Ratings / Leaderboard
# ---------------------------------------------------------------------------

def _format_seconds(seconds):
    """Format seconds into human-readable string."""
    if seconds is None or seconds <= 0:
        return '—'
    minutes, secs = divmod(int(seconds), 60)
    if minutes > 0:
        return f'{minutes} min {secs} sek'
    return f'{secs} sek'


def ratings(request):
    """Leaderboard page — user rankings grouped by quiz."""
    from django.db.models import Avg, Count as AggCount, F, ExpressionWrapper, fields

    category_slug = request.GET.get('category', '')

    # Get quizzes with results
    quizzes = Quiz.objects.select_related('category')
    if category_slug:
        quizzes = quizzes.filter(category__slug=category_slug)

    # Only quizzes that have at least one result
    quizzes = quizzes.filter(results__isnull=False).distinct()

    test_groups = {}
    for quiz in quizzes:
        # Get aggregated results per user for this quiz
        user_stats = (
            UserResult.objects
            .filter(quiz=quiz)
            .values('user__username')
            .annotate(
                avg_score_raw=Avg(
                    ExpressionWrapper(
                        F('score') * 100.0 / F('total'),
                        output_field=fields.FloatField()
                    )
                ),
                tests_completed=AggCount('id'),
                avg_duration=Avg(
                    ExpressionWrapper(
                        F('completed_at') - F('started_at'),
                        output_field=fields.DurationField()
                    )
                ),
            )
            .order_by('-avg_score_raw', 'avg_duration')
        )

        ratings_list = []
        for stat in user_stats:
            avg_dur = stat['avg_duration']
            avg_seconds = avg_dur.total_seconds() if avg_dur else None
            ratings_list.append({
                'username': stat['user__username'],
                'avg_score': stat['avg_score_raw'] or 0,
                'tests_completed': stat['tests_completed'],
                'avg_time_display': _format_seconds(avg_seconds),
            })

        if ratings_list:
            test_groups[quiz.title] = {
                'quiz_id': quiz.id,
                'ratings': ratings_list,
            }

    return render(request, 'ratings.html', {
        'test_groups': test_groups,
        'current_category': category_slug,
    })


import csv
from django.http import HttpResponse

def export_ratings(request):
    """Export ratings as CSV for a specific quiz."""
    from django.db.models import Avg, Count as AggCount, F, ExpressionWrapper, fields

    quiz_id = request.GET.get('quiz_id')
    if not quiz_id:
        return HttpResponse('quiz_id parametri kerak', status=400)

    quiz = get_object_or_404(Quiz, id=quiz_id)

    user_stats = (
        UserResult.objects
        .filter(quiz=quiz)
        .values('user__username')
        .annotate(
            avg_score_raw=Avg(
                ExpressionWrapper(
                    F('score') * 100.0 / F('total'),
                    output_field=fields.FloatField()
                )
            ),
            tests_completed=AggCount('id'),
            avg_duration=Avg(
                ExpressionWrapper(
                    F('completed_at') - F('started_at'),
                    output_field=fields.DurationField()
                )
            ),
        )
        .order_by('-avg_score_raw')
    )

    response = HttpResponse(content_type='text/csv; charset=utf-8')
    response['Content-Disposition'] = f'attachment; filename="ratings_{quiz.id}.csv"'
    response.write('\ufeff')  # BOM for Excel

    writer = csv.writer(response)
    writer.writerow(['Foydalanuvchi', "O'rtacha %", 'Topshirilgan', "O'rtacha vaqt (sek)"])

    for stat in user_stats:
        avg_dur = stat['avg_duration']
        avg_seconds = int(avg_dur.total_seconds()) if avg_dur else ''
        writer.writerow([
            stat['user__username'],
            f"{stat['avg_score_raw']:.1f}" if stat['avg_score_raw'] else '0',
            stat['tests_completed'],
            avg_seconds,
        ])

    return response


