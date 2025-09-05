from app.models import Color

def run():
    color_names = [
        "Red", "Blue", "Green", "Yellow", "Orange", "Purple", "Pink", "Brown",
        "Black", "White", "Gray", "Silver", "Gold", "Beige",
        "Cyan", "Magenta", "Teal", "Navy", "Indigo", "Violet",
        "Coral", "Salmon", "Khaki", "Olive", "Maroon", "Chocolate",
        "Plum", "Crimson", "Turquoise", "Lavender", "Mint",
        "Peach", "Skyblue", "Fuchsia"
    ]

    for c in color_names:
        obj, created = Color.objects.get_or_create(name=c)
        if created:
            print(f"✅ Added: {c}")
        else:
            print(f"⚡ Already exists: {c}")
