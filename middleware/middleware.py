from django.conf import settings

#from django.contrib.auth.models import User
import datetime

MAX_THRESHOLD = getattr(settings, 'MAX_THRESHOLD', 1000)
CURRENT_REQUEST_COUNT = getattr(settings, 'CURRENT_REQUEST_COUNT', 0)
TMIN = getattr(settings, 'TMIN', datetime.now)


class ThrowttleMiddleware(object):
    """
    Test Throttle
    """

    def process_request(self, request):
        print "HEYY"
        if CURRENT_REQUEST_COUNT < MAX_THRESHOLD:
            settings.CURRENT_REQUEST_COUNT = settings.CURRENT_REQUEST_COUNT+1
            print settings.CURRENT_REQUEST_COUNT
            if datetime.now - settings.TMIN > 1:
                settings.TMIN = datetime.now
                settings.CURRENT_REQUEST_COUNT = 0
        else:
            print "Throwttled"

        return None


