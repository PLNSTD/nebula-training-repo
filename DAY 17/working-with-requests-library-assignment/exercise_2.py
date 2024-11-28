import requests

post_id = 1
base_URL = f'https://jsonplaceholder.typicode.com/posts/{post_id}/comments'

response = requests.get(base_URL, timeout=4)

if response.status_code != 200:
    print(f'Failed to retrieve data. Status code: {response.status_code}')
    exit(0)

data = response.json()
new_comment_id = data[-1]['id']
new_comment_name = 'blabla'
new_comment_email = 'firstlast@gmail.com'
new_comment_body = "laudantium enim quasi est quidem magnam voluptate ipsam eos"
new_comment = {
    'postId': 1, 
    'id': 501, 
    'name': new_comment_name, 
    'email': new_comment_email,
    'body': new_comment_body
    }
post_response = requests.post(base_URL, json=new_comment, timeout=4)

if post_response.status_code != 201:
    print(f'Failed to create user. Status code: {post_response.status_code}')
    exit(0)

print('Comment created successfully.')
print(post_response.json())


new_comment['body'] = 'hello it s me mario'

try:
    base_URL = f'https://jsonplaceholder.typicode.com/posts/{post_id}/comments'
    put_response = requests.put(base_URL, json=new_comment, timeout=4)

    if put_response == 200 or put_response == 204:
        print('Comment updated successfully')
        print(put_response.json())
    else:
        put_response.raise_for_status()
except requests.exceptions.HTTPError: # Handles 404 error
    print(f'Comment not updated, code_status: {put_response.status_code}')

    