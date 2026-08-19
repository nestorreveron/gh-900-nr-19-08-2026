def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["data"]["status"] == "healthy"


def test_list_customers(client):
    response = client.get("/api/customers")
    assert response.status_code == 200
    assert len(response.json["data"]) == 200


def test_search_customers(client):
    response = client.get("/api/customers/search?q=contoso")
    assert response.status_code == 200
    assert response.json["data"]


def test_missing_customer(client):
    response = client.get("/api/customers/9999")
    assert response.status_code == 404
