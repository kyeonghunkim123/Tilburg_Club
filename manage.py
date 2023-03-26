#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    print('여기는 manage.py 파일 8번째줄')
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test.settings')
    try:
        from django.core.management import execute_from_command_line
        print('여기는 manage.py 파일 13번째줄')
    except ImportError as exc:
        print('여기는 manage.py 파일 15번째줄')
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    print('여기는 manage.py 파일 21번째줄')
    execute_from_command_line(sys.argv)
    print('여기는 manage.py 파일 23번째줄')


if __name__ == '__main__':
    main()
