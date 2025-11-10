class Service():
    def addition_service(self,a,b):
        c=a+b
        d={"status": "success","message":f"sum is {c}"}
        return d
    def subtraction_service(self,a,b):
        c=a-b
        d={"status": "success","message":f"sum is {c}"}
        return d


# --------------//-------------

#
# from django.contrib.auth.models import User
# from employees.models import AuthToken
# from django.contrib.auth import authenticate
#
# class AuthService:
#
#     def login_service(self, username, password):
#         user = authenticate(username=username, password=password)
#         if User.objects.filter(username=username).exists():
#             return {"error": "Username already exists"}
#         token = AuthToken.objects.get(user=user)
#         return {"token": token.token}
#
#     def register_service(self, username, password):
#         if User.objects.filter(username=username).exists():
#             return {"error": "Username already exists"}
#         user = User.objects.create_user(username=username, password=password)
#         token = AuthToken.objects.get(user=user)
#         return {"username": user.username, "token": token.token}
