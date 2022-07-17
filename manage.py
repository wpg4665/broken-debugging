#!/usr/bin/env python
import os
import sys
from pathlib import Path

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")

    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        import django
        raise

    current_path = Path(__file__).parent.resolve()
    sys.path.append(str(current_path / "test_project"))
    execute_from_command_line(sys.argv)
