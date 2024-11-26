### **Practical Exercises 📝**

1. **Analyzing API Documentation:**

   - **Task:** Review the documentation of a public API (e.g., GitHub API, OpenWeatherMap API).
   - **Objective:** Identify and list:
     - **Endpoints:** Key API endpoints available.
     - **HTTP Methods:** The methods used for each endpoint (GET, POST, etc.).
     - **Required Parameters:** Any mandatory parameters for requests.
     - **Expected Responses:** The format and structure of the data returned.

2. **Mapping HTTP Methods to CRUD Operations:**

   - **Task:** Create a table mapping the CRUD operations to the appropriate HTTP methods.
   - **Objective:** Understand how each HTTP method corresponds to create, read, update, and delete actions.

     | CRUD Operation | HTTP Method |
     | -------------- | ----------- |
     | Create         |             |
     | Read           |             |
     | Update         |             |
     | Delete         |             |

3. **Designing RESTful URIs:**

   - **Resources Provided:**
     - **Users**
     - **Posts**
     - **Comments**
     - **Categories**
     - **Tags**
   - **Task:** For each resource, design RESTful URIs for the following actions:
     - **Listing all items**
     - **Retrieving a specific item**
     - **Creating a new item**
     - **Updating an existing item**
     - **Deleting an item**
   - **Objective:** Practice constructing standard RESTful endpoints.

4. **Understanding Status Codes:**

   - **Scenarios:**
     1. **Resource Not Found:** A client requests a user profile that doesn't exist.
     2. **Unauthorized Access:** A client tries to access a protected resource without valid authentication.
     3. **Successful Creation:** A new post is successfully created on the server.
     4. **Bad Request:** A client sends a request with invalid syntax that the server cannot understand.
   - **Task:** Determine the appropriate HTTP status code for each scenario.
   - **Objective:** Familiarize yourself with common HTTP status codes and their meanings.
