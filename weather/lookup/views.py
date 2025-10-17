from django.shortcuts import render

def home(request):
	import json
	import requests

	# https://www.airnowapi.org/aq/observation/zipCode/current/?format=text/csv&zipCode=89129&distance=25&API_KEY=38DDFD4F-0056-4CF7-9DD4-055E0FA30422
	# https://www.airnowapi.org/aq/forecast/zipCode/?format=text/csv&zipCode=20002&date=2025-10-17&distance=25&API_KEY=38DDFD4F-0056-4CF7-9DD4-055E0FA30422


	api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=38DDFD4F-0056-4CF7-9DD4-055E0FA30422")

	try:
		api = json.loads(api_request.content)
	
	except Exception as e:
		api = "Error..."
	


	return render(request, 'home.html', {'api': api})

def about(request):
	return render(request, 'about.html', {})
