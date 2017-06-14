import requests

def get_api_data(url, post_id):

	try:
		check_value = int(post_id)

		response = requests.get(url + post_id)

	except :
		raise ValueError("Please enter whole numbers from 1 to 100")

	return response

def post_data_to_api(post_url, title, body):
	pass

def main():
	
	print "******** Command Line API Application ********"

	post_number = raw_input("Please enter a number between 1 and 100 \n")

	print "Fetching your the post you want....\n"
	
	response = get_api_data('https://jsonplaceholder.typicode.com/posts/', '3')

	print("\tGET Response data\n\t%s\n%s\n\tStatus code\n\t%s\n%s\n\tHeaders\n\t%s\n%s" % 
		("-"*17,response.text, "-"*11, response.status_code,"-"*7, response.headers))
	
	print "Looking good so far...."
	print "Now let's create a post"

	title = raw_input("Enter the title of your post: ")
	body = raw_input("Enter the body for your post: ")

	print("\n\tCreating your new post...\n")
	post_r = post_data_to_api('https://jsonplaceholder.typicode.com/posts/', title, body)
	print("\tPOST Response data\n\t%s\n%s\n\tStatus code\n\t%s\n%s\n\tHeaders\n\t%s\n%s" % 
		("-"*17,post_r.text, "-"*11, post_r.status_code,"-"*7, post_r.headers))




if __name__ == '__main__':
	main()