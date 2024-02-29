"""
django rest-framework configuration
"""
from src.settings import default

default.INSTALLED_APPS.extend([
    "rest_framework",
])
