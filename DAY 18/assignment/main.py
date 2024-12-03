import requests, json, os, platform, time

public_api_url = 'https://reqres.in'
get_user_path = '/api/users'
create_user_path = '/api/users'

def clear_terminal():
    if platform.system() == "Windows":
        os.system("cls")  # Clear terminal on Windows
    else:
        os.system("clear")  # Clear terminal on Unix/Linux/Mac

def main():
    # First assignment
    while True:
        clear_terminal()
        print('Option 1 - Get all Users')
        print('Option 2 - Create a User')
        print('Option 3 - Get Single User')
        print('Option 4 - Delete Single User')
        user_option = int(input('\nType the option number: '))
        print('\n\n')
        if user_option == 1:
            get_request_assignment()
        elif user_option == 2:
            username = input('Insert Username: ')
            job_title = input('Insert job title: ')
            post_request_assignment(username, job_title)
        elif user_option == 3:
            user_choice = int(input('Type the id of the user: '))
            get_single_user(user_choice)
        elif user_option == 4:
            user_choice = int(input('Type the id of the user to delete: '))
            delete_single_user(user_choice)
        time.sleep(4)

def post_request_assignment(name, job):
    create_user_url = public_api_url + create_user_path 

    payload = {
        'name': name,
        'job': job
    }

    # Check if the request was successful
    try:
        create_user_response = requests.post(create_user_url, json=payload, timeout=4)
        
        if create_user_response.status_code == 201:
            # Parse the JSON data
            data = create_user_response.json()
            file_name = 'user_creation_response.json'
            present_data(data, file_name)
            print(f'Response on file={file_name}')
        else:
            create_user_response.raise_for_status()
    except requests.exceptions.HTTPError:
        print(f'Failed to create data. Status code: {create_user_response.status_code}')
    except requests.exceptions.ConnectionError:
        print(f'Connection Error')

def get_request_assignment():
    get_user_url = public_api_url + get_user_path

    try: 
        get_user_response = requests.get(get_user_url)

        # Check if the request was successful
        if get_user_response.status_code == 200:
            # Parse the JSON data
            data = get_user_response.json()
            file_name = 'get_user_response.json'
            present_data(data, file_name)
            print(f'Response on file={file_name}')
        else:
            get_user_response.raise_for_status() # 404 
    except requests.exceptions.HTTPError: # 404
        print(f'Failed to retrieve data. Status code: {get_user_response.status_code}')
    except requests.exceptions.ConnectionError:
        print(f'Connection Error')

def present_data(data, file_name):

    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)

def get_single_user(id_number):
    single_user = public_api_url + f'/api/users/{id_number}'
    
    try:
        response = requests.get(single_user, timeout=4)
        if response.status_code == 200:
            data = response.json()
            file_name = 'get_single_user_response.json'
            present_data(data, file_name)
            print(f"Response on file = {file_name}")
        else:
            response.raise_for_status()
    except requests.exceptions.HTTPError:
        print(f"Failed to retreive: {response.status_code}")
    except requests.exceptions.ConnectionError:
        print(f"Connetion Error")

def delete_single_user(id_number):
    delete_url = public_api_url + f'/api/users/{id_number}'

    response = requests.delete(delete_url)

    if response.status_code == 204: # successfully deleted
        # data = response.json()
        # print(data)
        print(f'Successfully deleted, {response.status_code}')
    else:
        print('User not found OR User not deleted')

main()
