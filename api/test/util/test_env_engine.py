import os
import unittest
from os.path import join, abspath

from scalio.util.env_engine import EnvironmentEngine, EnvironmentException


class EnvironmentEngineTest(unittest.TestCase):

    def setUp(self):
        self._starting_environ = dict(os.environ)

    def tearDown(self):
        os.environ.clear()
        os.environ.update(self._starting_environ)

    def test_initialization_loads_variables_from_application_file(self):
        class TestEnvironemnt(EnvironmentEngine):
            test: str = None
        path = abspath(join(__file__, '..', 'res'))
        environment = TestEnvironemnt(resources_file=path, application_file_keyword='simple')
        self.assertEqual(environment.test, 'something')

    def test_initialization_loads_variables_from_environment_variables(self):
        class TestEnvironemnt(EnvironmentEngine):
            test: str = None
        os.environ['test'] = 'something'
        path = abspath(join(__file__, '..', 'res'))
        environment = TestEnvironemnt(resources_file=path, application_file_keyword='env')
        self.assertEqual(environment.test, 'something')

    def test_initialization_prefers_enviornment_variable_over_application_property_variable(self):
        class TestEnvironment(EnvironmentEngine):
            test: str = None
        os.environ['test'] = 'something2'
        path = abspath(join(__file__, '..', 'res'))
        environment = TestEnvironment(resources_file=path, application_file_keyword='simple')
        self.assertEqual(environment.test, 'something2')

    def test_initialization_throws_exception_when_variable_is_not_in_environment_variables_or_application_file(self):
        class TestEnvironemnt(EnvironmentEngine):
            test: str = None
        path = abspath(join(__file__, '..', 'res'))
        try:
            environment = TestEnvironemnt(resources_file=path, application_file_keyword='notempty')
            self.fail('Should throw exception when it cannot find a variable')
        except EnvironmentException as e:
            pass