import unittest, requests
from http_web import get_api_data, post_data_to_api

class HttpWebTestCase(unittest.TestCase):

	api_url = 'https://jsonplaceholder.typicode.com/posts'

	# Check for result from API
	def test_api_data(self):
		self.assertIsInstance(get_api_data(self.api_url, '3'), requests.models.Response, "200 OK from API can is reachable and accessible")

	# Check if error is raised for non int values
	def test_get_api_data_raises_error_non_int_values(self):
		with self.assertRaises(ValueError):
			get_api_data(self.api_url, 'abc')

	# Check for no result, 404
	def test_api_data_exceed_post_id(self):
		self.assertIsInstance(get_api_data(self.api_url, '310'), requests.models.Response, "Return response even though no data is NOT found on API")



