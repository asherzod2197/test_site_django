from .models import Category


def categories_processor(request):
    """Inject all categories into every template context."""
    return {'all_categories': Category.objects.all()}
