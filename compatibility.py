import sys

python_major_version = sys.version_info[0]

if python_major_version == 3:
  basestring = unicode = str