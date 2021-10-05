from django.http import HttpResponse
from django.shortcuts import redirect

def groups_required(allowed_groups=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            user_groups = None
            if request.user.groups.exists():
                user_groups = request.user.groups.all()
            # print(user_groups '\n', allowed_groups)
            for group in user_groups:
                if group.name in allowed_groups:
                    return view_func(request, *args, **kwargs)
            
            # if didn't return anything after looping & checking all groups, then no allowed group exists for this user 
            return HttpResponse("You are not authorised to view this page.")
        return wrapper_func
    return decorator