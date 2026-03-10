class SimpleMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code before view runs
        print("Request received")

        response = self.get_response(request)

        # Code after view runs
        print("Response sent")

        return response
