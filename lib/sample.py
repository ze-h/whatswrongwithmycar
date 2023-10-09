import requests

URL = "https://vpic.nhtsa.dot.gov/api/"

# Returns the number of cylinders in a 2013 BMW X3
def x3() -> str:
    arg = "vehicles/decodevin/5UXWX7C5*BA?format=json&modelyear=2011"
    try:
        response = requests.get(url=(URL + arg), timeout=30)
    except(requests.Timeout):
        return None
    return response.json().get("Results")[70].get("Value")
