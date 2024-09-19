# User Management API

A simple FastAPI application for managing users.

## Endpoints

### Get All Users

* **GET /users/**
	+ Retrieve a list of all users
	+ Response: A list of user objects

### Get a Single User

* **GET /users/search**
	+ Retrieve a single user by ID, name, or email
	+ Query Parameters:
		- `id`: The ID of the user to retrieve
		- `name`: The name of the user to retrieve
		- `email`: The email of the user to retrieve
	+ Response: A single user object

### Create a New User

* **POST /users/**
	+ Create a new user
	+ Request Body: A user object
	+ Response: The newly created user object

### Update an Existing User

* **PUT /users/{id}**
	+ Update an existing user
	+ Path Parameters:
		- `id`: The ID of the user to update
	+ Request Body: A user object
	+ Response: The updated user object

### Delete a User

* **DELETE /users/{id}**
	+ Delete a user
	+ Path Parameters:
		- `id`: The ID of the user to delete
	+ Response: A success message

## User Object

* `id`: The ID of the user
* `name`: The name of the user
* `email`: The email of the user

## Error Handling

* **400 Bad Request**: If a request is invalid or missing required parameters
* **404 Not Found**: If a user is not found

## Dependencies

* FastAPI
* Pydantic
* MongoDB

## Running the Application

1. Install the dependencies using pip: `pip install fastapi pydantic pymongo`
2. Start the application using uvicorn: `uvicorn main:app --host 0.0.0.0 --port 8000`
3. Access the API documentation at http://localhost:8000/docs

## MongoDB Index Creation

To improve the performance of queries, create the following indexes on the `users` collection:

### Create Index on _id Field

db.users.createIndex({ _id: 1 })

### Create Index on name Field

db.users.createIndex({ name: 1 })

### Create Index on email Field

db.users.createIndex({ email: 1 })