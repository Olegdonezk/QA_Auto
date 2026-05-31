from typing import Any, Dict
import requests


class EmployeeApi:
    BASE_URL = "http://5.101.50.27:8000"

    def __init__(self, username, password):
        self.session = requests.Session()
        # Автоматически логинимся при создании объекта класса
        self._login(username, password)

    def _login(self, username, password):
        """Приватный метод для авторизации и получения токена"""
        response = self.session.post(
            f"{self.BASE_URL}/auth/login",
            json={"username": username, "password": password},
        )
        # Если логин неуспешный (например, 400 или 500), код упадет здесь с ошибкой
        response.raise_for_status()

        # Сохраняем полученный токен в атрибуты класса
        data = response.json()
        self.client_token = data["user_token"]

    def create_employee(self, employee_data: Dict[str, Any]):
        """POST /employee/create"""
        url = f"{self.BASE_URL}/employee/create"
        return self.session.post(url, json=employee_data)

    def get_employee(self, employee_id: int):
        """GET /employee/info/{employee_id}"""
        url = f"{self.BASE_URL}/employee/info/{employee_id}"
        return self.session.get(url)

    def update_employee(self, employee_id: int, update_data: Dict[str, Any]):
        """PATCH /employee/change/{employee_id}"""
        url = f"{self.BASE_URL}/employee/change/{employee_id}"

        # Передаем настоящий токен, который получили при логине
        params = {"client_token": self.client_token}
        return self.session.patch(url, params=params, json=update_data)

    def get_employee_list(self, company_id: int):
        """GET /employee/list/{company_id}"""
        url = f"{self.BASE_URL}/employee/list/{company_id}"
        return self.session.get(url)