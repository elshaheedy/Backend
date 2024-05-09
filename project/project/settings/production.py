"""
Production settings for the project.

This module contains settings specific to the production environment.
"""

import dj_database_url
from decouple import config

db_config = dj_database_url.config(default=config("DATABASE_URL"))

db_config['ATOMIC_REQUESTS'] = True
DATABASES = {
    'default': db_config,
    
}
