from django.shortcuts import redirect

class LanguageRedirectMiddleware:
    """
    Redirect users to choose_language page if they haven't selected a language yet.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ignored_paths = [
            '/choose_language/',
            '/set_language/',
            '/admin/',
            '/static/',
            '/media/',
        ]

        # Only redirect if language not chosen and path is not ignored
        if not request.session.get('language_chosen', False):
            if not any(request.path.startswith(path) for path in ignored_paths):
                return redirect('choose_language')

        response = self.get_response(request)
        return response
