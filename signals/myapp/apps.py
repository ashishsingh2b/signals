# myapp/apps.py

from django.apps import AppConfig

class BlogConfig(AppConfig):
    name = 'myapp'
    
    def ready(self):
        import myapp.signals  # Import your signals module when the app is ready
