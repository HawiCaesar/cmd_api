import requests

# Runs a get request and returns result
def get_api_data(url, post_id):

	try:
		check_value = int(post_id)

		response = requests.get(url + post_id)

	except :
		raise ValueError("Please enter whole numbers from 1 to 100")

	return response

# Runs a post request and returns a result
def post_data_to_api(post_url, title, body):
	post_data = {
			'title': title,
			'body': body,
			'userId': 1
		}
	response = requests.post(post_url, data=post_data)

	return response

def main():
	
	print "******** Command Line Http Web API App ********"

	post_number = raw_input("Please enter a number between 1 and 100 \n")

	print "Fetching your the post you want....\n"
	
	response = get_api_data('https://jsonplaceholder.typicode.com/posts/', '3')

	print "Headers"
	print response.headers
	print "-"*15
	print "Status Code"
	print response.status_code
	print "-"*15
	print "GET Response data"
	print response.text
	print "-"*15
	
	print "Looking good so far...."
	print "Now let's create a post"

	title = raw_input("Enter the title of your post: ")
	body = raw_input("Enter the body for your post: ")

	print("\n\tCreating your new post...\n")
	post_response = post_data_to_api('https://jsonplaceholder.typicode.com/posts/', title, body)

	print "Headers"
	print post_response.headers
	print "-"*15
	print "Status Code"
	print post_response.status_code
	print "-"*15
	print "GET Response data"
	print post_response.text
	print "-"*15

	print "\n\n\n"

	print "Good Stuff! Thank you for consuming the API"




if __name__ == '__main__':
	main()