from . import TestRanger


class TestRangerAPI(TestRanger):

    def test_storage(self):
        post_data = {
            "identifier": "foo",
            "ranges": [[12,34],[37,440],[460,800]]
        }
        url = '/store'
        resp = self.app.post_json(url, post_data)

    def test_ranger(self):
        post_data = {
            "identifier": "foo",
            "ranges": [[12,34],[37,440],[460,800]]
        }
        url = '/store'
        resp = self.app.post_json(url, post_data)
        assert( resp.status_code == 200 )

        req = "440,464"
        url = '/v1/get_intersections/{}'.format(req)
        resp = self.app.get(url)
        assert( resp.status_code == 200 )

        # check result
        intersections = [x.get('intersection') for x in resp.json['result']]
        assert( intersections == [5] )

