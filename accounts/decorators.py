from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_func):
    """
    Decorator allows only unauthenticated users access registration and login pages.
    Authenticated users get redirected to home page.
    """
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


def allowed_users(allowed_roles=[]):
    """Identify users that have permissions to access different parts of the website"""
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You don\'t have a permission to access this page')
                
        return wrapper_func
    return decorator

    
    
    
    
    
    

        
        
           
 
       
        



