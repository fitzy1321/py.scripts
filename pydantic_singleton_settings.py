from devtools import debug
from pydantic_settings import BaseSettings

# DO NOT IMPORT FROM HERE
# There is a global apisettings object in api/__init__.py/
# Please import as `from api import api_settings`


class APISettings:
    """
    I couldn't figure out how to dynamically
    add fields to a `BaseSettings` model.

    So, I made a wrapper a pydantic Settings obejct instead.

    It is also a Singleton, so all intsance of this class
    show have the same values.

    It doesn't make sense to instansiate multiple settings objeects,
    when these settings should never change after startup.
    """

    _instance = None

    class Settings(BaseSettings):
        # conn_str = ""
        # username = ""
        # password = ""
        # env = ""

        class Config:
            env_file = ".env"

        # @validator("*")
        # def must_have_value(cls, v):
        #     if v in [None, ""]:
        #         raise ValueError("Env variables not loaded.")
        #     return v

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(APISettings, cls).__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        self._settings = self.Settings()
        # self.app_name = f"{self._settings.env}.app.com"


settings = APISettings()
debug(settings)
