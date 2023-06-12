#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import logging
from django.conf import settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

def configure_logger():
    """
    Configures the logger for the application.
    
    Returns:
        The configured logger object.
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(settings.LOGGING['loggers']['project']['level'])

    # Check if the logger already has the handler
    if not logger.handlers:
        handler = logging.FileHandler(settings.LOGGING['handlers']['file']['filename'])
        handler.setLevel(settings.LOGGING['handlers']['file']['level'])

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        logger.addHandler(handler)
    
    return logger

def main():
    """
    Main function to run administrative tasks.
    """
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        logger.exception("An error occurred: %s", str(exc))
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    logger.info("Server is starting...")
    try:
        execute_from_command_line(sys.argv)
    except Exception as e:
        logger.exception("An error occurred: %s", str(e))
        sys.exit(1)


if __name__ == "__main__":
    logger = configure_logger()
    main()
