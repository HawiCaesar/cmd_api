import unittest, requests
from http_web import get_api_data, post_data_to_api

class HttpWebTestCase(unittest.TestCase):

	api_url = 'https://jsonplaceholder.typicode.com/posts/'

	# Check for result from API
	def test_api_data(self):
		self.assertIsInstance(get_api_data(self.api_url, '3'), requests.models.Response, "Data from API can is reachable and accessible")

	# Check if error is raised for non int values
	def test_get_api_data_raises_error_non_int_values(self):
		with self.assertRaises(ValueError):
			get_api_data(self.api_url, 'abc')

	# Check for no result, 404
	def test_api_data_exceed_post_id(self):
		self.assertIsInstance(get_api_data(self.api_url, '310'), requests.models.Response, "Return response even though no data is NOT found on API")

	# Check for 200OK result
	def test_api_data_correct_response200OK(self):
		response = get_api_data(self.api_url, '4')

		self.assertEqual(response.status_code, 200, "200 OK response for reachable API")

	# Check for 404 not found result
	def test_api_data_correct_response404(self):
		response = get_api_data(self.api_url, '310')

		self.assertEqual(response.status_code, 404, "404 response no post found")

