from engine.mastercard_api_demos import example_lost, example_score

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


def invoke_mastercard_api(name, params={}):
    """
    Invokes Mastercard API's example code

    NOTE:
        1. In case no params are passed, default params are picked up from the demo code
        2. Any exception triggered in demo code is returned back

    :param name: name of the API to invoke
    :param params: dictionary of parameters, defaults to {}
    :return res: result dictionary to be passed to durable rules

    :raises Exception
    """
    try:
        if "lost" in name:
            res = example_lost(params)
        elif "score" in name:
            res = example_score(params)
        return res
    except Exception:
        raise