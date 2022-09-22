def validate_request(request):
    if not request.headers.get('Content-type') or request.headers.get('Content-type') != 'application/json':
        return {"code": 415, "message":  "Type not supported for app"}
    elif request.get_json() == {}:
        return {"code": 500, "message":  "Internal Server Error"}

    return None
