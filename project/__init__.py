from django.apps import AppConfig


class ProjectConfig(AppConfig):
    name = 'project'
    verbose_name = 'Проджект'

default_app_config = 'project.ProjectConfig'