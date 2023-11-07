import random
from fastapi.testclient import TestClient
import sys


sys.path.append("./")
sys.path.append("../")
from app.main import app
from app.database.schemas import Answer

client = TestClient(app)


# def test_get_user():
#     response = client.get("/user")
#     assert response.status_code == 200


# def test_get_challenge():
#     user = client.get("/user").json()
#     access_token = user["api_token"]
#     challenge = client.get(
#         "/challenge", headers={"Authorization": "Bearer " + access_token}
#     )
#     assert challenge.status_code == 200


# def test_not_get_challenge():
#     user = client.get("/user").json()
#     # access_token = user["api_token"]
#     challenge = client.get(
#         "/challenge", headers={"Authorization": "Bearer " + "hogehoge"}
#     )
#     assert challenge.status_code != 200


# def test_get_quiz():
#     user = client.get("/user").json()
#     access_token = user["api_token"]
#     challenge = client.get(
#         "/challenge", headers={"Authorization": "Bearer " + access_token}
#     )
#     challenge_id = challenge.json()["challenge_id"]
#     res = client.get(
#         f"/challenge/{challenge_id}/quiz",
#         headers={"Authorization": "Bearer " + access_token},
#     )
#     quizzes = res.json()
#     assert res.status_code == 200
#     # 5問あるか
#     assert len(quizzes) == 5
#     # 一つの問題の選択肢は4つか？
#     for q in quizzes:
#         assert len(q) == 4


def test_get_quiz():
    user = client.get("/user").json()
    access_token = user["api_token"]
    challenge = client.get(
        "/challenge", headers={"Authorization": "Bearer " + access_token}
    )
    challenge_id = challenge.json()["challenge_id"]
    res = client.get(
        f"/challenge/{challenge_id}/quiz",
        headers={"Authorization": "Bearer " + access_token},
    )
    quizzes = res.json()

    answers = []
    # quizzes =
    # [{'quiz_id': 86, 'move_id': 218, 'id': 341},
    #  {'quiz_id': 86, 'move_id': 183, 'id': 342},
    #  {'quiz_id': 86, 'move_id': 278, 'id': 343},
    #  {'quiz_id': 86, 'move_id': 347, 'id': 344}]
    for q in quizzes:
        d = {
            "quiz_id": q[0]["quiz_id"],
            "answer_move_id": q[random.randint(0, 3)]["move_id"],
        }
        answers.append(d)

    # print({"challenge_id": challenge_id, "answers": answers})
    res = client.post(
        f"/challenge/{challenge_id}/answer",
        json={"challenge_id": challenge_id, "answers": answers},
        headers={"Authorization": "Bearer " + access_token},
    )

    assert res.status_code == 200
