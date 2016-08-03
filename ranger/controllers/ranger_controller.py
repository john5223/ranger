from bottle import get, post
from bottle import request, response, HTTPError

from services import storage
from services import intersector


def get_intersection(req_data, version=None):
    #validate
    if not isinstance(req_data, list):
        body = "Incorrect req_data. Not List."
        response.status = 500
        return body
    if len(req_data) != 2:
        body = "Incorrect range length. Must be in formart [start, end]"
        response.status = 500
        return body
    try:
        req_data = [int(x) for x in req_data]
    except ValueError as e:
        response.status = 500
        return "Must be integer ranges"

    # return response
    # ie. [{"identifier": "foo","ranges":[[37,440],[460,800]],"intersection":5}]
    result = intersector.get_intersections(req_data, version=version)
    print result
    return {'result': result }


@get('/<version>/get_intersections/<req_data>')
def get_intersection_v1(version, req_data):
    req_data = req_data.split(',')
    return get_intersection(req_data, version=version)


@post('/<version>/get_intersections')
def post_intersection_v1(version):
    req_data = request.json
    # req_data = [440, 464]
    result = intersector.get_intersections(req_data, version=version)
    return {"result" : result}


@post('/store')
def store_identifier():
    resp = storage.store(request.json)
    return {'status': 'succes'}


