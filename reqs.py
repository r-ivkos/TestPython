import requests

ADDRESS = "http://127.0.0.1:5000/"

inp = input()
while inp:
	if inp == "GET":
		response = requests.get(ADDRESS+"tasks/")
		print(response.json())
	elif inp == "POST":
		inp = input("POST: ")
		response = requests.post(ADDRESS+"create_task/", {"name":inp})
		print(response.json())
	elif inp == "PUT":
		inp = input("PUT: ")
		response = requests.put(ADDRESS+"task/"+inp)
		print(response.json())
	elif inp == "PATCH":
		inp = input("PATCH: ")
		response = requests.patch(ADDRESS+"task/"+inp)
		print(response.json())
	inp = input()
