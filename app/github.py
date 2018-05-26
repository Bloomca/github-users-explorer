import requests
from .exceptions import NotFoundException

def get_user_data(id):
  return get_user_repos(id)

def get_user_repos(username):
  url = "/users/{username}/repos".format(username=username)
  return make_github_request(url)

def make_github_request(url, **kwargs):
  headers = {'Accept': 'application/vnd.github.v3+json'}

  if 'headers' in kwargs:
    headers = {**headers, **kwargs['headers']}

  prefix = "https://api.github.com"

  r = requests.get(prefix + url, headers=headers, **kwargs)

  if r.status_code == 404:
    raise NotFoundException("This user does not exist")

  return r.json()
  
