import sys

activate_this = '/home/ubuntu/.virtualenvs/hello_flask_env/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

sys.path.insert(0, "/var/www/headlines_flask")
from headlines import app as application

