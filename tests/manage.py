#!/usr/bin/env python
# vim: set et ts=4 sw=4 fileencoding=utf-8:
'''
Manage for test django project
'''
import os
import sys
try:
    import settings  # pylint: disable=unused-import,relative-import
except ImportError:
    sys.stderr.write("Error importing settings")
    sys.exit(1)

# add the parent directory to sys.path so that the test module has
# natural_key_cache in it's python path
TESTDIR = os.path.dirname(__file__)
MODULEDIR = os.path.dirname(TESTDIR)
sys.path.insert(0, MODULEDIR)

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
