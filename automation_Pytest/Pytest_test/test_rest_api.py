import requests

ENDPOINT = "https://todo.pixegami.io/"

response=requests.get(ENDPOINT)
print(response)


status =response.status_code
print(status)


def test_can_call_endpoint():
    response=requests.get(ENDPOINT)
    assert response.status_code == 200

def test_can_create_task():
    payload=new_task_payload()
    create_task_response =create_task(payload)
    assert create_task_response.status_code == 200

    data =create_task_response.json()
    print(data)
    task_id = data["task"]["task_id"]

    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 200

    get_task_data = get_task_response.json()

    assert get_task_data["content"] == payload["content"]
    assert get_task_data["user_id"] == payload["user_id"]


def create_task(payload):
        return requests.put(ENDPOINT + "/create-task",json=payload)

def get_task(task_id):
        return requests.get(ENDPOINT + f"/get-task/{task_id}")

def update_task(payload):
    return requests.put(ENDPOINT + "/update-task",json=payload)

def list_task(user_id):
   return requests.get(ENDPOINT + f"/get-task/{user_id}")

def new_task_payload():
    return {
        "content":"my new contents",
        "user_id":"test_users",
        "is_done":False
        }

def test_can_update_task():
    payload=new_task_payload()
    create_task_response = create_task(payload)
    task_id = create_task_response.json()['task']['task_id']

    new_payload={
        "user_id":payload["user_id"],
        "task_id":task_id,
        "content":"my updated content",
        "is_done":True
    }

    update_task_response = update_task(new_payload)
    assert update_task_response.status_code == 200

    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 200

    get_task_data = get_task_response.json()
    assert get_task_data["content"] == new_payload["content"]
    assert get_task_data["user_id"] == new_payload["user_id"]


def test_can_list_tasks():
    N=3
    for i in range(N):
        payload=new_task_payload()
        create_task_response =create_task(payload)
        assert create_task_response.status_code == 200
    
    list_task_response= list_task("test_users")
    assert list_task_response.status_code == 200
    data =list_task_response.json()
    tasks =data['tasks']
    assert len(tasks)==N










































