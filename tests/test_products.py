def test_list_products(client):
    response = client.get("/api/products")
    assert response.status_code == 200
    assert len(response.json["data"]) == 50


def test_get_product(client):
    response = client.get("/api/products/1")
    assert response.status_code == 200
    assert response.json["data"]["name"].startswith("Contoso")
