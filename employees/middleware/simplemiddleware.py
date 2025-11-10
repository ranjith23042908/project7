class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Decode body to string
        content = response.content.decode()

        # Append middleware info
        content += f"\nMiddleware: Active"
        content += f"\nMethod: {request.method}"
        content += f"\nPath: {request.path}"

        # Convert back to bytes
        response.content = content.encode()

        # Optional: add custom header too
        response["X-Simple-Middleware"] = "Active"

        return response


import json
from django.http import JsonResponse

class JsonMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Only modify if response is JSON
        if 'application/json' in response.get('Content-Type', ''):
            # Decode original JSON
            try:
                data = json.loads(response.content)
            except Exception:
                data = {}

            # Add middleware info
            data["_middleware"] = {
                "status": "Active",
                "method": request.method,
                "path": request.path
            }

            # Return modified JSON response
            response = JsonResponse(data)

        # Add optional header
        response["X-Simple-Middleware"] = "Active"

        return response

