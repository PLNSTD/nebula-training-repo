# Working with the `requests` Library 🐍

## Learning Outcomes 🎯

- **Master the fundamentals of the `requests` library to send HTTP requests from Python, covering GET, POST, PUT, DELETE, and other methods.**
- **Practice sending requests to retrieve and submit data to RESTful APIs and process JSON/XML responses efficiently.**
- **Learn to handle API errors and status codes appropriately, incorporating best practices for robust and error-tolerant code.**
- **Understand how to authenticate requests and manage sessions when interacting with APIs.**

---

### Introduction 📝

In this lecture, we'll delve into the practical aspects of interacting with Web APIs using Python's `requests` library. Building on the conceptual understanding of Web APIs and RESTful principles from the previous lecture, we'll now focus on implementing these concepts in code.

The `requests` library is a powerful and user-friendly HTTP client library that simplifies making HTTP requests in Python. It abstracts much of the complexity of handling HTTP requests and responses, making it an essential tool for any Python developer working with web services.

---

### Installing the `requests` Library 📦

Before using the `requests` library, ensure it's installed in your Python environment. You can install it using `pip`:

```bash
pip install requests
```

---

### Sending HTTP Requests 🚀

#### Basic Structure of a Request 🧩

A typical HTTP request using the `requests` library involves specifying:

- **Method**: The type of request (e.g., GET, POST).
- **URL**: The endpoint of the API.
- **Headers**: (Optional) Additional information sent with the request.
- **Data/Payload**: (Optional) The data sent with the request (for POST, PUT, PATCH methods).
- **Parameters**: (Optional) Query parameters appended to the URL.

---

#### GET Requests 📥

GET requests are used to retrieve data from a server. Here's how to send a basic GET request:

```python
import requests

url = 'https://api.example.com/data'
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON data
    data = response.json()
    print(data)
else:
    print(f'Failed to retrieve data. Status code: {response.status_code}')
```

**Adding Query Parameters**

You can include query parameters in your GET request using the `params` argument:

```python
params = {'search': 'python', 'limit': 10}
response = requests.get(url, params=params)
```

---

#### POST Requests 📤

POST requests are used to send data to the server, typically to create a new resource.

```python
import requests

url = 'https://api.example.com/users'
payload = {'name': 'John Doe', 'email': 'john.doe@example.com'}
response = requests.post(url, json=payload)

if response.status_code == 201:
    print('User created successfully.')
    print(response.json())
else:
    print(f'Failed to create user. Status code: {response.status_code}')
```

**Note:** When sending JSON data, use the `json` parameter. For form-encoded data, use the `data` parameter.

---

#### PUT and PATCH Requests ✏️

- **PUT** is used to update an entire resource.
- **PATCH** is used to make partial updates to a resource.

```python
# PUT Request
url = 'https://api.example.com/users/123'
payload = {'name': 'Jane Doe', 'email': 'jane.doe@example.com'}
response = requests.put(url, json=payload)

# PATCH Request
payload = {'email': 'jane.newemail@example.com'}
response = requests.patch(url, json=payload)
```

---

#### DELETE Requests 🗑️

DELETE requests are used to remove a resource from the server.

```python
url = 'https://api.example.com/users/123'
response = requests.delete(url)

if response.status_code == 204:
    print('User deleted successfully.')
else:
    print(f'Failed to delete user. Status code: {response.status_code}')
```

---

### Handling Responses 📬

#### Parsing JSON Responses 🗂️

The `response` object contains the server's response to your HTTP request. If the response content is in JSON format, you can parse it using:

```python
data = response.json()
```

#### Accessing Response Headers 📨

You can access response headers using:

```python
headers = response.headers
print(headers['Content-Type'])
```

#### Binary Content 📷

For responses containing binary data (e.g., images), use:

```python
content = response.content
with open('image.png', 'wb') as file:
    file.write(content)
```

---

### Handling Errors and Exceptions ⚠️

#### Status Codes 🛎️

Always check the `status_code` to determine if the request was successful.

```python
if response.status_code == requests.codes.ok:
    # Success
else:
    # Handle errors
```

#### Raising Exceptions for HTTP Errors 🚨

Use `raise_for_status()` to raise an `HTTPError` exception for bad responses (4xx and 5xx status codes).

```python
try:
    response.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(f'HTTP error occurred: {err}')
except Exception as err:
    print(f'Other error occurred: {err}')
```

#### Common Exceptions 🛑

- `requests.exceptions.ConnectionError`: Failed to connect to the server.
- `requests.exceptions.Timeout`: The request timed out.
- `requests.exceptions.TooManyRedirects`: Exceeded the maximum number of redirects.
- `requests.exceptions.RequestException`: Base exception that catches all other exceptions.

---

### Timeouts and Retries ⏲️

#### Setting Timeouts ⌛

Specify a timeout to prevent your program from waiting indefinitely:

```python
response = requests.get(url, timeout=5)  # Timeout after 5 seconds
```

#### Implementing Retries 🔄

For robust applications, you may want to retry requests that fail due to network errors. Use the `requests` library in conjunction with `urllib3`'s `Retry` functionality.

```python
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

session = requests.Session()
retry = Retry(total=3, backoff_factor=0.3, status_forcelist=[500, 502, 504])
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

response = session.get(url)
```

---

### Session Objects 🗂️

Use a `Session` object to persist parameters across requests, such as cookies and headers.

```python
session = requests.Session()
session.headers.update({'Authorization': 'Bearer YOUR_API_TOKEN'})

response = session.get(url)
```

---

### Authentication 🔑

#### Basic Authentication 📝

```python
response = requests.get(url, auth=('username', 'password'))
```

#### Token-Based Authentication 🛡️

Include tokens in headers:

```python
headers = {'Authorization': 'Bearer YOUR_API_TOKEN'}
response = requests.get(url, headers=headers)
```

---

### Uploading Files 📁

You can upload files using the `files` parameter.

```python
files = {'file': open('report.csv', 'rb')}
response = requests.post(url, files=files)
```

---

### Working with SSL Verification 🔒

By default, `requests` verifies SSL certificates. To disable SSL verification (not recommended):

```python
response = requests.get(url, verify=False)
```

---

### Best Practices 🏆

1. **Use Timeouts**

   Always specify a timeout for your requests to prevent hanging indefinitely.

   ```python
   response = requests.get(url, timeout=10)
   ```

2. **Validate SSL Certificates**

   Avoid disabling SSL verification unless necessary, and be cautious when doing so.

3. **Handle Exceptions**

   Use try-except blocks to catch and handle exceptions gracefully.

4. **Manage Sessions**

   Use `Session` objects to persist configurations and improve performance.

5. **Respect Rate Limits**

   Be mindful of the API's rate limits to avoid being throttled or banned. Implement delays if necessary.

6. **Secure Your Credentials**

   Do not hardcode API keys or passwords in your scripts. Use environment variables or configuration files.

7. **Logging**

   Implement logging to track your application's behavior and troubleshoot issues.

---

### Conclusion 🎉

By mastering the `requests` library, you can effectively interact with Web APIs, enabling your Python applications to communicate over the internet. This lecture covered the practical aspects of sending various types of HTTP requests, handling responses, managing errors, and following best practices for robust and secure code.

---

### Additional Resources 📚

- **Requests Documentation**: [http://docs.python-requests.org/en/master/](http://docs.python-requests.org/en/master/)
- **HTTP Status Codes**: [https://developer.mozilla.org/en-US/docs/Web/HTTP/Status](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
- **Public APIs for Practice**: [https://github.com/public-apis/public-apis](https://github.com/public-apis/public-apis)
