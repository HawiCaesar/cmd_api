import unittest 
from http_web import get_api_data, post_data_to_api

class HttpWebTestCase(unittest.TestCase):

	url = 'ioio'

	# Check for 200 OK result from API
	def test_api_data_200OK(self):
		self.assertEqual(get_api_data(url, 3), "<Response [200]>", "200 OK from API can is reachable and accessible")




