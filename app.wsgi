import sys
import site
import os

site.addsitedir('/var/www/1periode/env/lib/python3.13/site-packages')

sys.path.insert(0, '/var/www/1periode')

os.chdir('/var/www/1periode')

os.environ['VIRTUAL_ENV'] = '/var/www/1periode/env'
os.environ['PATH'] = '/var/www/1periode/env/bin:' + os.environ['PATH']

from app import app as application
