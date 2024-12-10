# Уксусов Евгений, 24А-я когорта — Инженер по тестированию плюс. Финальный проект.

# Автотест
def test_order_creation_and_retrieval():
    response = create_new_order(data.order_body)

    track_number = response.json()["track"]
    print("Заказ создан. Номер заказа:", track_number)

# Получение данных заказа по треку
    order_response = get_order(track_number)

    assert order_response.status_code == 200, f"Ошибка: {order_response.status_code}"
    order_data = order_response.json()
    print("Данные заказа:")
    print(order_data)
