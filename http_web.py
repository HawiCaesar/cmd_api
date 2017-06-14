import requests

def get_api_data(url, post_id):

	response = requests.get(url + post_id)
	return response
		

def post_data_to_api(post_url):
	pass

def main():
	get_api_data('https://jsonplaceholder.typicode.com/posts/', '3')



if __name__ == '__main__':
	main()