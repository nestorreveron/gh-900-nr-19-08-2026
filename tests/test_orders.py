def test_create_order(client):
    response = client.post("/api/orders", json={"customer_id": 1, "product_id": 1, "quantity": 2})
    assert response.status_code == 201
    assert response.json["data"]["quantity"] == 2
    assert response.json["data"]["total"] > 0


def test_order_validation(client):
    response = client.post("/api/orders", json={"customer_id": 1, "product_id": 1, "quantity": 0})
    assert response.status_code == 400
    assert "quantity must be a positive integer" in response.json["errors"]
