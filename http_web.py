import requests

def get_api_data(url, post_id):

	r = requests.get(url + post_id)
	print(r)
		

def post_data_to_api(post_url, title, body, userId=11):
	post_data = {
		'title': title,
		'body': body,
		'userId': userId
		}
	r = requests.post(post_url, data=post_data)
	return r

def main():
	get_api_data('https://jsonplaceholder.typicode.com/posts/', 'tyt')



if __name__ == '__main__':
	main()