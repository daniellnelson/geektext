from django.apps import AppConfig


class GeekprofileConfig(AppConfig):
    name = 'geekprofile'

    def ready(self):
        import users.signals
