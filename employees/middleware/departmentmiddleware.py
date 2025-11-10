import json
from django.http import JsonResponse, HttpResponse

class DepartmentMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Only handle GET requests to department endpoint
        if request.method == "GET" and request.path.startswith("/employees/get_show_department"):
            try:
                # Convert string content to Python object
                data = json.loads(response.content.decode())
            except Exception:
                data = {}

            # Add middleware info
            data["middleware"] = {
                "status": "Active",
                "method": request.method,
                "path": request.path
            }

            # Return clean JSON response
            response = JsonResponse(data)
            response["X-Department-Middleware"] = "Active"
        return response
