import requests

def get_api_data(url, post_id):

	try:
		check_value = int(post_id)

		response = requests.get(url + post_id)

	except ValueError as e:
		raise(e)
		response = "No post macthes your request.Please enter an integer."

	return response

def post_data_to_api(post_url):
	pass

def main():
	"""

	print "******** Command Line API Application ********"

	post_number = raw_input("Please enter a number between 1 and 100 \n")

	print "Fetching your the post you want....\n"
	"""

	response = get_api_data('https://jsonplaceholder.typicode.com/posts/', '3')

	




if __name__ == '__main__':
	main()