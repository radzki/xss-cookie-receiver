from pydantic_settings import BaseSettings, SettingsConfigDict


class MailingConfig(BaseSettings):
    class Config:
        env_prefix = "MAILING_"

    api_key: str


class APIConfig(BaseSettings):
    class Config:
        env_prefix = "API_"

    url: str


class Config(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    mailing: MailingConfig = MailingConfig()
    api: APIConfig = APIConfig()


app_config: Config = Config()
