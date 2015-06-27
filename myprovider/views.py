from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponse

class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('{ "login": "username", "email": "happy@example.com", "name": "Hong Gil", "id": "1234" }')
#        return HttpResponse('Hello, OAuth2!')
#        return HttpResponse('{}')
