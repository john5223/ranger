import json
from bottle import error, response

@error('401')
@error('402')
@error('404')
@error('500')
@error('505')
def error_json(error):
    ret = {
        'error': error.status,
        'status': error.status_code
    }
    response.content_type = 'application/json'
    return json.dumps(ret)

