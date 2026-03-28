from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=120, unique=True)
    description = models.CharField(max_length=300, blank=True, default='')

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name


class Quiz(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy', 'Oson'),
        ('medium', "O'rta"),
        ('hard', 'Qiyin'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, default='')
    markdown_file = models.CharField(max_length=300, blank=True, default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='quizzes')
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES, default='medium')
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = 'Quizzes'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def question_count(self):
        return self.questions.count()


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    question_md = models.TextField()
    option_a = models.TextField()
    option_b = models.TextField()
    option_c = models.TextField()
    option_d = models.TextField(blank=True, default='')
    correct_option = models.CharField(max_length=1)
    explanation_md = models.TextField(blank=True, default='')
    order_index = models.IntegerField(default=0)

    class Meta:
        ordering = ['order_index']

    def __str__(self):
        return f"Q{self.order_index}: {self.question_md[:60]}"


class UserResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='results')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='results')
    score = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    started_at = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-completed_at']

    def __str__(self):
        return f"{self.user.username} — {self.quiz.title}: {self.score}/{self.total}"

    def percentage(self):
        if self.total == 0:
            return 0
        return round(self.score / self.total * 100)

    def duration_seconds(self):
        """Return duration in seconds, or None if started_at is not set."""
        if self.started_at and self.completed_at:
            delta = self.completed_at - self.started_at
            return int(delta.total_seconds())
        return None

    def duration_display(self):
        """Return human-readable duration string."""
        seconds = self.duration_seconds()
        if seconds is None:
            return '—'
        minutes, secs = divmod(seconds, 60)
        if minutes > 0:
            return f'{minutes} min {secs} sek'
        return f'{secs} sek'
