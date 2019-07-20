from django.apps import AppConfig


class FbAppConfig(AppConfig):
    name = "fb"

    def ready(self):
        from fb import signals # pylint: disable=unused-variable
