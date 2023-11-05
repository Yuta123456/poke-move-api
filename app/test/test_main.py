from fastapi.testclient import TestClient
import sys


sys.path.append("./")
sys.path.append("../")
from app.main import app

client = TestClient(app)


def test_get_user():
    response = client.get("/user")
    assert response.status_code == 200


def test_get_challenge():
    user = client.get("/user").json()
    access_token = user["api_token"]
    challenge = client.get(
        "/challenge", headers={"Authorization": "Bearer " + access_token}
    )
    assert challenge.status_code == 200


def test_not_get_challenge():
    user = client.get("/user").json()
    # access_token = user["api_token"]
    challenge = client.get(
        "/challenge", headers={"Authorization": "Bearer " + "hogehoge"}
    )
    assert challenge.status_code != 200


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
    assert res.status_code == 200
    # 5問あるか
    assert len(quizzes) == 5
    # 一つの問題の選択肢は4つか？
    for q in quizzes:
        assert len(q) == 4
