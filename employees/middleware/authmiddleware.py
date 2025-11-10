# from django.http import JsonResponse
# from employees.models import AuthToken
#
# class AuthMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request):
#         # Skip auth for login and admin
#         if request.path.startswith("/login") or request.path.startswith("/admin"):
#             return self.get_response(request)
#
#         # Print debug to check headers
#         print("Headers received:", request.headers)
#
#         auth_header = request.headers.get("Authorization")
#         if not auth_header:
#             return JsonResponse({"error": "Missing Authorization header"}, status=401)
#
#         if not auth_header.startswith("Token "):
#             return JsonResponse({"error": "Invalid Authorization format"}, status=401)
#
#         provided_token = auth_header.split(" ")[1]
#
#         try:
#             AuthToken.objects.get(token=provided_token)
#         except AuthToken.DoesNotExist:
#             return JsonResponse({"error": "Unauthorized"}, status=401)
#
#         return self.get_response(request)
