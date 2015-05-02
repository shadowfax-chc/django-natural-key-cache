#!/usr/bin/env python
# vim: set et ts=4 sw=4 fileencoding=utf-8:
import os
import sys
try:
    import settings
except ImportError:
    sys.stderr.write("Error importing settings")
    sys.exit(1)

# add the parent directory to sys.path so that the test module has autocache
# in it's python path
testdir = os.path.dirname(__file__)
moduledir = os.path.dirname(testdir)
sys.path.insert(0, moduledir)

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
