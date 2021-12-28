import os

from django.core.wsgi import get_wsgi_application

path = '/home/path/to/project'
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hello.settings')

application = get_wsgi_application()
