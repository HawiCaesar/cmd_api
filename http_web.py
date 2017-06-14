import requests

def get_api_data(url, post_id):

	if post_id.isdigit():

		response = requests.get(url + post_id)
		return response

	else:
		try:
			int(post_id)
			response = requests.get(url + post_id)
			return response

		except ValueError as error:
			return "No post macthes your request.Please enter an integer."
		

def post_data_to_api(post_url):
	pass

def main():

	print "******** Command Line API Application ********"

	post_number = raw_input("Please enter a number between 1 and 100 \n")

	print "Fetching your the post you want....\n"

	response = get_api_data('https://jsonplaceholder.typicode.com/posts/', post_number)
	print("\tGET Response data\n\t%s\n%s\n\tStatus code\n\t%s\n%s\n\tHeaders\n\t%s\n%s" % 
		("-"*17,response.text, "-"*11,response.status_code,"-"*7, response.headers))

	print "Looks like everything is ok and good to go"
	




if __name__ == '__main__':
	main()