from pydantic import BaseSettings


class Settings(BaseSettings) :
    OPENAI_API_KEY: str

    class Config :
        env_file = 'file.env'
        # env_file_encoding = 'utf-8'


# setting = Settings(_env_file='file.env', _env_file_encoding='utf-8')
setting = Settings()
