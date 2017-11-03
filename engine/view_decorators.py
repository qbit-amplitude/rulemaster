from functools import wraps
from django.http import JsonResponse
from engine.utils import generate_response_dict


def require_http_methods(http_methods_list):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view_func(request, *args, **kwargs):
            if request.method not in http_methods_list:
                if len(http_methods_list) == 1:
                    http_methods_string = http_methods_list[0]
                else:
                    http_methods_string = " or ".join(http_methods_list)
                error = {
                    "message": "Only {} method allowed.".format(http_methods_string)
                }
                resp = generate_response_dict(http_status=405, success=False,
                                              response="Method Not Allowed", error=error)
                return JsonResponse(resp, status=405)
            else:
                return view_func(request, *args, **kwargs)
        return _wrapped_view_func
    return decorator