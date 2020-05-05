from django.http import HttpResponse
from django.shortcuts import redirect

# def allowed_users(allowed_roles=[]):
#     def decorator(view_func):
#         def wrapper_func(request, *args, **kwargs):
            
#             group = None
#             if request.user.group.exist():
#                 group = request.user.group.all().name
                
#             if group in allowed_roles:
#                 return view_func(request, *args, **kwargs)
#             else:
#                 return HttpResponse('Not authorised')
            
#         return wrapper_func
#     return decorator


# add decorator with the user type which is allowed for each section in a same way as log in required

# user types are:
################ staff
################ paying_member
################ registered_user