import json

# global error
error = {}


class ReqResStandardMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    # If used with MIDDLEWARE_CLASSES, the __call__() method will never be used;
    # Django calls process_request() and process_response() directly.
    def __call__(self, request):
        """
        Code to be executed for each request before the view (and later
        middleware) are called.
        """
        print('a')
        request = self.process_request(request)
        print('b')
        response = self.get_response(request)
        print('c')
        response = self.process_response(request, response)
        print('d')
        return response

    def process_request(self, request):
        request.META['HTTP_CUSTOM_HEADER'] = {
            'meta': {},
        }
        # import pdb
        # pdb.set_trace()
        print("from here")
        # print(request.META)
        return request

    def process_response(self, request, response):

        res_obj = {}
        global error
        print(error)
        if error:
            res_obj = {
                'meta': {},
                'data': {},
                'errors': str(error),
                'status': response.status_code,
            }
            error = {}
        else:
            print(response.data)
            res_obj = {
                "meta": {},
                # "data": response.data,
                "errors": [],
                "status": response.status_code,
            }

        print(response._headers)
        #response._header is not mutable
        # https://stackoverflow.com/questions/36099244/how-to-add-an-http-header-to-all-django-responses/36099405
        response['HTTP_CUSTOM_HEADER'] = {'meta': {}}
        response.content = json.dumps(res_obj)
        print(response.content)
        print(response['HTTP_CUSTOM_HEADER'])
        return response

    def process_exception(self, request, exception):
        print('e')
        global error
        error = exception
        print(exception)
