from django.contrib.auth.models import User


class EmailAuth:
    """Authenticate user by email"""
    
    def Authenticate(self, username=None, password=None):
        """Get user by email and verify password"""
        
        try:
            user = User.objects.get(email=username)
            
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None
        
    def get_user(self, user_id):
        """Django retrieves user"""
        
        try:
            user = User.objects.get(pk=user_id)
            
            if user.is_active:
                return user
            return None
        except User.DoesNotExist:
            return None
        