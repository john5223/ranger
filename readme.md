Ranger
=======

API to find intersection count between ranges

POST to store object identifier and associated ranges:

{"identifier": "foo",
 "ranges": [[12,34],[37,440],[460,800]]}

GET to find intersection count amonst known identifiers:

Request: [440, 464]

Response: [{”identifier”: ”foo”,”ranges”:[[37,440],[460,800]],”intersection”:5}]

Example API requests
============
Store identifier
```
curl 127.0.0.1:8088/store -X POST -H "Content-type: application/json" -d '{"identifier": "foo","ranges": [[12,34],[37,440],[460,800]]}'
```


Find intersection count amonst identifiers:
```
> curl 127.0.0.1:8088/v1/get_intersections/440,464
{"result": [{"ranges": [[37, 440], [460, 800]], "intersection": 5, "identifier": "foo"}]}
```



Install requirements
====================
pip install -r requirements.txt


Run Tests
==========
nosetests tests/ -sv

Example run:
```
> nosetests tests -sv

tests.test_ranger.TestRangerAPI.test_ranger ...
[{'ranges': [(37, 440), (460, 800)], 'intersection': 5, 'identifier': 'foo'}]
ok
tests.test_ranger.TestRangerAPI.test_storage ... ok
tests.test_ranger_errors.TestRangerAPIErrors.test_noninteger_inputs ... ok
tests.test_ranger_errors.TestRangerAPIErrors.test_too_many_inputs ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.065s

OK

```

Run API (dev)
============
python2 ranger/api.py

Example run:
```
> python2 ranger/api.py
Bottle v0.12.8 server starting up (using GeventServer())...
Listening on http://127.0.0.1:8088/
Hit Ctrl-C to quit.

127.0.0.1 - - [2016-08-02 21:02:39] "POST /store HTTP/1.1" 200 128 0.000827
[{'ranges': [(37, 440), (460, 800)], 'intersection': 5, 'identifier': 'foo'}]
127.0.0.1 - - [2016-08-02 21:02:40] "GET /v1/get_intersections/440,464 HTTP/1.1" 200 197 0.001197


```



TODO
======

Try numba JIT compilation for CPU bound tasks

URL: numba.pydata.org
