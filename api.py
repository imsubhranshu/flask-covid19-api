try:
    import requests
    from bs4 import BeautifulSoup as bs
    import json
except:
    print("Module Could not be imported")

req = requests.get('https://api.covid19india.org/state_district_wise.json').content


soup = bs(req, 'html.parser')

file = soup.get_text()

data = json.loads(file)

#FOR STATE WISE DATA

# state = input("Enter state: ")
# date = input("Enter date(YYYY-MM-DD): ")

# confirmed = data[state]["dates"][date]['total']['confirmed']
# dead = data["OR"]["dates"]["2020-08-15"]['total']['deceased']
# recovered = data["OR"]["dates"]["2020-08-15"]['total']['recovered']
# tested = data["OR"]["dates"]["2020-08-15"]['total']['tested']

# print("Confirm case: ", confirmed)

states = data.keys()

def get_states():
    return list(states)

def get_district(state):
    district = data[state]['districtData']
    return list(district.keys())

def get_result(state, district):
    result : dict
    fetch = data[state]['districtData'][district]
    result = fetch
    result_now = fetch['delta']
    return result


print(get_district('Odisha'))


