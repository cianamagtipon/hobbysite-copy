from django.apps import AppConfig


class UserManagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_management'

    def ready(self):
        # Import signals to ensure signal handlers are connected.
        import user_management.signals
