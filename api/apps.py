from django.apps import AppConfig

class ApiConfig(AppConfig):
    name = 'api'

    # def ready(self):
    #     from modules import updater
    #     updater.start()