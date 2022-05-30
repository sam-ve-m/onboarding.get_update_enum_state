import os
from pathlib import Path

from dotenv import load_dotenv
from decouple import Config, RepositoryEnv


class Configuration:
    config = None

    @classmethod
    def get_config(cls, env_path: str = Path(__file__).parent.absolute()):
        path = os.path.join(env_path, ".env")
        path = str(path)
        load_dotenv(path)
        cls.set_config(path)

    @classmethod
    def set_config(cls, env_path: str):
        cls.config = Config(RepositoryEnv(env_path))
