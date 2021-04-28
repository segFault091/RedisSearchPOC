import os

from grift import EnvLoader, JsonFileLoader
from grift.utils import in_same_dir


def get_settings_loaders():
    """Return a list of settings loader objects for this environment."""
    # Pull configuration from env, then test settings file (if testing), then a settings file
    LOCAL_CONFIG_PATH = in_same_dir(__file__, "local_config.json")
    SETTINGS_PATH = os.environ.get("SETTINGS_PATH", LOCAL_CONFIG_PATH)
    loaders = [EnvLoader(), JsonFileLoader(SETTINGS_PATH)]
    return loaders
