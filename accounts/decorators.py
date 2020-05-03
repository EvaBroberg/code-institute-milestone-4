from django.http import HttpResponse
from django.shortcuts import redirect

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                # change to redirect
                return HttpResponse('You are not authorised')
                
            
            
            
        return wrapper_func
    return decorator


# add decorator with the user type which is allowed for each section in a same way as log in required

# user types are:
################ staff
################ guest
################ paying_member
################ registered_user