from scalio.util.env_engine import EnvironmentEngine


class Environment(EnvironmentEngine):
    database_url: str = None


env = Environment()
