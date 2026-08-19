def test_create_ticket(client):
    response = client.post(
        "/api/support",
        json={"customer_id": 1, "subject": "Training ticket", "description": "Demo support case"},
    )
    assert response.status_code == 201
    assert response.json["data"]["status"] == "open"


def test_update_ticket(client):
    response = client.patch("/api/support/1", json={"status": "resolved"})
    assert response.status_code == 200
    assert response.json["data"]["status"] == "resolved"


def test_dashboard(client):
    response = client.get("/api/dashboard")
    assert response.status_code == 200
    assert response.json["data"]["customers"] == 200
    assert response.json["data"]["products"] == 50
    assert response.json["data"]["orders"] == 500
