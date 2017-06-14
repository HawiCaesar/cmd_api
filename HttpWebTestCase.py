import unittest, requests
from http_web import get_api_data, post_data_to_api

class HttpWebTestCase(unittest.TestCase):

	url = 'https://jsonplaceholder.typicode.com/posts'

	# Check for result from API
	def test_api_data_200OK(self):
		self.assertIsInstance(get_api_data(self.url, '3'), requests.models.Response, "200 OK from API can is reachable and accessible")




