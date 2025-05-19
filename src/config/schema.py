"""
Config Schema (Optional/Future)

Defines optional Pydantic models if structured config is added later.

Currently unused — .env is the only required config layer.
"""

from pydantic import BaseModel


# Future config model placeholder
class AppConfig(BaseModel):
    pass
