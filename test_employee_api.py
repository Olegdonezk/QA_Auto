import pytest
from employee_api import EmployeeApi


@pytest.fixture(scope="module")
def api():

    return EmployeeApi("harrypotter", "expelliarmus")


@pytest.fixture
def sample_employee_data():

    return {
        "first_name": "Тестовый",
        "last_name": "Пользователь",
        "company_id": 1,
        "email": "test.qa@example.com",
        "phone": "+79161234567",
        "birthdate": "1995-06-20",
        "is_active": True,
    }


@pytest.mark.integration
def test_employee_creation(api, sample_employee_data):
    """Тест создания нового сотрудника"""
    response = api.create_employee(sample_employee_data)

    assert (
        response.status_code == 200
    ), f"Создание не удалось: {response.status_code} - {response.text}"

    data = response.json()
    assert data["first_name"] == sample_employee_data["first_name"]
    assert data["email"] == sample_employee_data["email"]
    assert data.get("is_active") is True

    print("\n✅ Сотрудник успешно создан")


@pytest.mark.integration
def test_employee_update(api):
    """Тест обновления сотрудника"""
    employee_id = 1


    original_data = api.get_employee(employee_id).json()
    original_email = original_data.get("email")


    new_email = "updated_qa_user@example.com"
    patch_data = {"email": new_email}

    response = api.update_employee(employee_id, patch_data)

    assert response.status_code == 200, f"""
    Обновление не удалось!
    Status: {response.status_code}
    Ответ: {response.text}
    """


    get_response = api.get_employee(employee_id)
    assert get_response.status_code == 200

    updated = get_response.json()
    assert updated.get("email") == new_email

    print(f"✅ Успешно обновлён сотрудник ID = {employee_id}")
    print("Обновлённые данные:", updated)


    api.update_employee(employee_id, {"email": original_email})