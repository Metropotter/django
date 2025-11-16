from django.shortcuts import render, get_object_or_404
from .models import Language


def home(request):
    languages = Language.objects.all()
    return render(request, 'languages_app/home.html', {'languages': languages})


def language_detail(request, language_id):
    language = get_object_or_404(Language, id=language_id)

    # INCREMENT VIEW COUNT when someone visits the page
    language.increment_view_count()

    return render(request, 'languages_app/language_detail.html', {'language': language})


def popular_languages(request):
    """Show 3-5 most viewed languages (actual popularity based on views)"""

    # Get languages ordered by view count (most popular first)
    popular_langs = Language.objects.all().order_by('-view_count')[:5]

    return render(request, 'languages_app/popular_languages.html', {
        'languages': popular_langs,
        'popular_count': popular_langs.count()
    })