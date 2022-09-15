
from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="HARAMBOT",
    settings_files=['settings.toml', '.secrets.toml'],
    environments=True,
)