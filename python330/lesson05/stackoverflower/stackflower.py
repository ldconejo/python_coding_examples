import requests

keyword = input("What term do you want to search for? ").strip()

response = requests.get(f"https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&tagged={keyword}&site=stackoverflow")

question = response.json()['items'][0]

json_response = response.json()

completed_queries = {
    'django ' : json_response
}

title = question['title']
user_id = question['owner']['user_id']
display_name = question['owner']['display_name']

response = requests.get(f"https://api.stackexchange.com/2.3/users/{user_id}?order=desc&sort=reputation&site=stackoverflow")

creation_date = response.json()['items'][0]['creation_date']

print(f"{display_name} created on {creation_date} asked \"{title}\"")