from dotenv import find_dotenv
from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class OpenAISettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=find_dotenv(),
        case_sensitive=False,
        extra='ignore'
    )

    api_key: SecretStr = Field("<TOKEN>", alias="OPENAI_API_KEY")


openai_settings = OpenAISettings()
