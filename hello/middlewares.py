import json
from rest_framework.views import APIView


class ReqResStandardMiddleware(APIView):
    def __init__(self, get_response):
        self.get_response = get_response
        # return super(ReqResStandardMiddleware, self).__init__(get_response)

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        d = request.POST
        print(d.__dict__)
        response = self.get_response(request)
        # Code to be executed for each request/response after
        # the view is called.
        response.data['value'] = 567
        # print(response.status)
        res_obj = {
            "meta": {},
            "data": response.data,
            "errors": [],
            "status": response.status_code,
        }
        response.content = json.dumps(res_obj)
        return response
