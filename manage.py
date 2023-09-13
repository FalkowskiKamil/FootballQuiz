import os
import sys
import threading
from utils.mongo_connection import checking_connection

def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    try:
        connection_thread = threading.Thread(target=checking_connection)
        connection_thread.start()
        execute_from_command_line(sys.argv)
    except Exception as e:
        sys.exit(1)


if __name__ == "__main__":
    main()