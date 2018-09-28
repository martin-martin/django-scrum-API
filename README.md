# Django Scrum board API

* task board with different columns
* moving tasks through different columns
* different 'states' can track the progress of a task
* the preceding tasks have to be part of a taskf for it to become 'completed'

## Tasks
Tasks will have a couple of different states:

* Not Started
* In Progress
* Testing
* Done

## API Design

```py
/api/
    /sprints/
        /<id>/
    /tasks/
        /<id>/
    /users/
        /<username>/
```

## API query

Querying the API from a CL interface.

E.g. adding a new Sprint using POST

```
Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 03:03:55)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import requests
>>> r = requests.get("http://localhost:8000/api/")
>>> r.headers
{'Date': 'Fri, 28 Sep 2018 10:35:31 GMT', 'Server': 'WSGIServer/0.2 CPython/3.6.5', 'Content-Type': 'application/json', 'Vary': 'Accept', 'Allow': 'GET, HEAD, OPTIONS', 'X-Frame-Options': 'SAMEORIGIN', 'Content-Length': '134'}
>>> r.status_code
200
>>> api = r.json()
>>> from pprint import pprint
>>> pprint(api)
{'sprints': 'http://localhost:8000/api/sprints/',
 'tasks': 'http://localhost:8000/api/tasks/',
 'users': 'http://localhost:8000/api/users/'}
>>> requests.get(api['sprints'])
<Response [401]>
>>> requests.get(api['sprints'], auth=('demo', 'test'))
<Response [200]>
>>> response = requests.get(api['sprints'], auth=('demo', 'test'))
>>> pprint(response.json())
[{'description': 'One week of getting everyone caught up with using Django as '
                 'an awesome tool for Web Dev.',
  'end': '2018-10-05',
  'id': 1,
  'links': {'self': 'http://localhost:8000/api/sprints/1/',
            'tasks': 'http://localhost:8000/api/tasks/?sprint=1'},
  'name': 'Django Week'}]
```

Adding a new Task using POST
```
>>> # ... continued from above...
>>> import datetime
>>> today = datetime.date.today()
>>> two_weeks = datetime.timedelta(days=14)
>>> data = {'name': 'Great Sprint', 'end': today + two_weeks}
>>> response = requests.post(api['sprints'], data=data, auth=('demo', 'test'))
>>> response.status_code
201
>>> sprint = response.json()
>>> pprint(sprint)
{'description': '',
 'end': '2018-10-12',
 'id': 2,
 'links': {'self': 'http://localhost:8000/api/sprints/2/',
           'tasks': 'http://localhost:8000/api/tasks/?sprint=2'},
 'name': 'Great Sprint'}
>>> data = {'name': 'Something Task', 'sprint': sprint['id']}
>>> response = requests.post(api['tasks'], data=data, auth=('demo', 'test'))
>>> response.status_code
201
>>> task = response.json()
>>> pprint(task)
{'assigned': None,
 'completed': None,
 'description': '',
 'due': None,
 'id': 3,
 'links': {'assigned': None,
           'self': 'http://localhost:8000/api/tasks/3/',
           'sprint': None},
 'name': 'Something Task',
 'order': 0,
 'started': None,
 'status': 1,
 'status_display': 'Not Started'}
 ```

 Try other HTTP verbs and queries using the CLI.
