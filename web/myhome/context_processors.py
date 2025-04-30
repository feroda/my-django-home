from django.conf import settings
from django.apps import apps


def export_settings(request):
    SUBTITLES_MAP = {
        "me": str(request.user),
        "districts": "Aree territoriali"}

    subtitle = ' '.join(request.path.split('/')[:2]).strip()
    subtitle = SUBTITLES_MAP.get(subtitle.lower(), subtitle).title()

    rv = {
        'BASE_URL': settings.BASE_URL,
        'API_BASE_URL': settings.API_BASE_URL,
        'MEDIA_BASE_URL': settings.MEDIA_URL,
        "is_prod": request.get_host() in (
            'lucaferroni.it', 
            'lucafero.it', 
            'ferodafabriano.it',
            'lucaferodafabriano.it',
            'lucaferroni.org', 
            'lucafero.org', 
            'ferodafabriano.org',
            'lucaferodafabriano.org',
        )
    }

    return rv
