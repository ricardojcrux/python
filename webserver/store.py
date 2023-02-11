import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    categories = r.json()
    for category in categories:
        print(category['id'],category['name'])
        