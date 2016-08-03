import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"../ranger")))

from webtest import TestApp

class TestRanger(object):

    @classmethod
    def setUpClass(self):
        import api
        self.app = TestApp(api.app)
        self.headers = [('Content-type', 'application/json')]


    @classmethod
    def tearDownClass(self):
        pass

