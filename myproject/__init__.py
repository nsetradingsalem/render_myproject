from .celery_settings import app as celery_app
 
__all__ = ['celery_app']

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery_settings import app as celery_app
from myproject.settings import *

__all__ = ('celery_app',)