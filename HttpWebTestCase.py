import unittest, requests
from http_web import get_api_data, post_data_to_api

class HttpWebTestCase(unittest.TestCase):

	url = 'https://jsonplaceholder.typicode.com/posts'

	# Check for result from API
	def test_api_data(self):
		self.assertIsInstance(get_api_data(self.url, '3'), requests.models.Response, "200 OK from API can is reachable and accessible")

	# Check for no result, 404
	def test_api_data_no_data_returned(self):
		self.assertEqual(get_api_data(self.url, 'abc'), "No post macthes your request.Please enter an integer.", "No post is found because of non-integers")



