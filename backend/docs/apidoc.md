# Husansvar Flask API
This documentation describes how to use the endpoints provided by this flask api.


The endponts of the api are accessable from the following base url:
`http://localhost:5000/api/v1`.


## Tasks
The tasks part allows other systems to access and manipulate the stored tasks in this system.

| URL (after base) | METHOD | Description          | Params | Return Success | Return failure |
| ---------------- | ------ | -------------------- | ------ | -------------- | -------------- |
| /tasks           | GET    | Get all tasks        | user   | 200            | 404            |
| /tasks           | POST   | Create a new task    |        | 200            | 404            |
| /tasks/{slug}    | GET    | Get a single task    |        | 200            | 404            |
| /tasks/{slug}    | PUT    | Edit a single task   |        | 200            | 404, 400       |
| /tasks/{slug}    | DELETE | Delete a single task |        | 204            | 404, 405       |

### Details
**GET TASKS**

The user may get all stored tasks by accessing the task endpoint, accessable from
`/tasks`.

**Param user:**

on the get request, the parameter user may be specified. If so, the api will behave in the following manner:
- If the user does not specify a user, all tasks are returned.
- If the user specifies a valid user as a parameter, only tasks belonging to said user will be returned.
- If an invalid user is requested or no tasks are stored, 404 and no data found will be returned.


**CREATE TASK**

To create a task, pass a task in json format to the `/tasks` endpoint. The api will assign the task a slug and add it to storage. The task along with its slug will be returned. If the sent json does not contain a title attribute, the api will return failure and 404.

**GET/PUT/DELETE TASK**

To get, edit or delete a single task, use the `/tasks/{slug}` endpoint, were slug is the slug belonging to the task.
(Slugs are created from the api, and does not have to be created by the client). These will behave as expected. If the slug does not exist, the get, put and delete requests will return 404.
The put request will return status code 400 if the data sent is not allowed.
The delete request will return 405 if the method is not allowed. As no information is sent after a successful delete request, the response returns statuscode 204.


