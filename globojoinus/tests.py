from testutils.testcase import _TestCase

class ViewTest(_TestCase):
    
    def test_home_responde_200(self):
        self.get("/globocom/404.hml")
        
    def test_home_responde_200(self):
        self.get("/globocom/quemfaz")

