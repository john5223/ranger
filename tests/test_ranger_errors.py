from .test_ranger import TestRanger


class TestRangerAPIErrors(TestRanger):

    def test_noninteger_inputs(self):
        url = '/v1/get_intersections/1,a'
        resp = self.app.get(url, expect_errors=True)
        assert( resp.status_code == 500)

    def test_too_many_inputs(self):
        url = '/v1/get_intersections/1,2,3'
        resp = self.app.get(url, expect_errors=True)
        assert( resp.status_code == 500)
