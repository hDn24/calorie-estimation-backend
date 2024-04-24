from pydantic import BaseSettings, Field


class Configs(BaseSettings):
    HOST: str = Field(default="0.0.0.0")
    PORT: int = Field(default=8000)

    DETECTION_THRESHOLD: float = Field(default=0.3)
    NUM_THREADS: int = Field(default=4)

    class Config:
        """How to read environment values."""

        env_file = ".env"
        allow_mutation = False


CFG = Configs()
