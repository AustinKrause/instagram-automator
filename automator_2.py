from instagram_private_api import Client, ClientCompatPatch

user_name = 'user_name'
password = 'pw'

api = Client(user_name, password)
results = api.feed_timeline()
items = results.get('items', [])
for item in items:
    # Manually patch the entity to match the public api as closely as possible, optional
    # To automatically patch entities, initialise the Client with auto_patch=True
    ClientCompatPatch.media(item)
    print(media['code'])

#print(api.authenticated_user_id)