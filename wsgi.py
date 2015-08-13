from __future__ import unicode_literals

import os
import sys

#sys.path.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'scout'))
sys.path.append(os.environ['OPENSHIFT_REPO_DIR'])
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()


# PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
# settings_module = "%s.settings" % PROJECT_ROOT.split(os.sep)[-1]
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)
#
# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()
