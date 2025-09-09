from .translations import translations

def lang_processor(request):
    lang = request.session.get("lang", "en")
    return {"t": translations[lang]}
