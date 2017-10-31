from django.conf import settings

#from django.contrib.auth.models import User
import datetime
from django.http import HttpResponseForbidden

class ThrowttleMiddleware(object):
    """
    Test Throttle
    """
    def process_request(self, request):
        diff = datetime.datetime.now() - settings.TMIN
        if settings.CURRENT_REQUEST_COUNT < settings.MAX_THRESHOLD and diff.seconds <=600 :
            settings.CURRENT_REQUEST_COUNT = settings.CURRENT_REQUEST_COUNT+1
            print "Current count limit :"+str(settings.CURRENT_REQUEST_COUNT)
        elif diff.seconds > 600:
                print "Before resetting count limit : "+str(settings.CURRENT_REQUEST_COUNT)
                print "Seconds : "+ str(diff.seconds)
                settings.TMIN = datetime.datetime.now()
                settings.CURRENT_REQUEST_COUNT = 0
                print "Current count limit :"+str(settings.CURRENT_REQUEST_COUNT)
        else:
            print "Throwttled"
            return HttpResponseForbidden()
        return None


