# Husansvar Flask API
This documentation describes how to use the endpoints provided by this flask api.


The endponts of the api are accessable from the following base url:
`{baseurl}/api/{version}`

- The current version is <b>v1</b>.

## Tasks
The tasks part allows other systems to access and manipulate the stored tasks in this system.

| URL (after base) | METHOD | Description          | Params | Return Success | Return failure |
| ---------------- | ------ | -------------------- | ------ | -------------- | -------------- |
| /tasks           | GET    | Get all tasks        | user   | 200            | 404            |
| /tasks           | POST   | Create a new task    |        | 200            | 404            |
| /tasks/{slug}    | GET    | Get a single task    |        | 200            | 404            |
| /tasks/{slug}    | PUT    | Edit a single task   |        | 200            | 404            |
| /tasks/{slug}    | DELETE | Delete a single task |        | 204            | 404            |

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

To create a task, pass a task in json format to the `/tasks` endpoint. The api will assign the task a slug and add it to storage. The task along with its slug will be returned.

**GET/PUT/DELETE TASK**

To get, edit or delete a single task, use the `/tasks/{slug}` endpoint, were slug is the slug belonging to the task.
(Slugs are created from the api, and does not have to be created by the client). These will behave as expected.

