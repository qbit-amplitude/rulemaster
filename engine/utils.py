def generate_response_dict(http_status, success, response, data=None,
                           error=None):
    response_dict = {}
    response_dict["http_status"] = http_status
    response_dict["success"] = success
    response_dict["response"] = response
    if not error:
        response_dict["data"] = data
    else:
        response_dict["error"] = error
    return response_dict