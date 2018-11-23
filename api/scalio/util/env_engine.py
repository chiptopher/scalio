
import os
from os.path import abspath, join

import yaml


class EnvironmentException(Exception):
    pass


class EnvironmentEngine:

    def __init__(self, resources_file: str=abspath(join(__file__, '..', '..', 'resources')), application_file_keyword=''):
        keyword = ''
        if application_file_keyword is not '':
            keyword = '-{}'.format(application_file_keyword)
        application_properties_file = join(resources_file, 'application{}.yml'.format(keyword))
        self._load_environment_variables(application_properties_file)

    def _load_environment_variables(self, application_properties_file):
        members = [attr for attr in dir(self) if
                   not callable(getattr(self, attr)) and not attr.startswith("__") and not attr.startswith('_')]
        for member in members:
            try:
                self._load_from_system_environment(member)
            except KeyError:
                try:
                    self._load_environment_variable_from_properties_file(application_properties_file, member)
                except KeyError:
                    message = '[{}] variable not present in properties file or environment variables'.format(member)
                    raise EnvironmentException(message)

    def _load_environment_variable_from_properties_file(self, application_properties_file, member):
        with open(application_properties_file, 'r') as stream:
            result = yaml.load(stream)
            setattr(self, member, result[member])

    def _load_from_system_environment(self, member):
        setattr(self, member, os.environ[member])
