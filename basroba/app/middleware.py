from django.shortcuts import redirect
from django.urls import reverse

class LanguageRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ignored_paths = [
            '/choose_language/',
            '/set_language/',   # skip set_language POST
            '/admin/',
            '/static/',
            '/media/',
        ]

        if not request.session.get('language_chosen', False):
            if not any(request.path.startswith(path) for path in ignored_paths):
                return redirect('choose_language')

        response = self.get_response(request)
        return response

