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
