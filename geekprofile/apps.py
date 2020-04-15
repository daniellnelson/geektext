from django.apps import AppConfig


class GeekprofileConfig(AppConfig):
    name = 'geekprofile'

    def ready(self):
        import geekprofile.signals
