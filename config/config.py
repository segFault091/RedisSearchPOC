from grift import BaseConfig, ConfigProperty
from schematics.types import IntType, StringType

from config.settings_loader import get_settings_loaders


class ExternalSearchConfig(BaseConfig):
    # REDIS App Settings
    REDIS_HOST = ConfigProperty(property_type=StringType())
    REDIS_PASSWORD = ConfigProperty(required=False, exclude_from_varz=True)
    REDIS_PORT = ConfigProperty(property_type=IntType(), default=6379)

    def __init__(self, loaders):
        """Initialize BaseConfig and metrics"""
        BaseConfig.__init__(self, loaders)


app_config = ExternalSearchConfig(get_settings_loaders())
