import requests
import pytest

BASE_URL = "https://web-production-ec481.up.railway.app/accounts"

@pytest.mark.parametrize("account_number", ["12345", "67890"])
def test_check_balance(account_number):
    response = requests.get(f"{BASE_URL}/{account_number}/balance")
    assert response.status_code == 200
    data = response.json()
    assert "balance" in data
    assert data["account_number"] == account_number

@pytest.mark.parametrize("account_number, deposit_amount", [
    ("12345", 100),
    ("67890", 200)
])
def test_deposit(account_number, deposit_amount):
    response = requests.post(f"{BASE_URL}/{account_number}/deposit", json={"amount": deposit_amount})
    assert response.status_code == 200
    data = response.json()
    assert data["account_number"] == account_number
    assert data["new_balance"] > 0  # ensure balance increased

@pytest.mark.parametrize("account_number, withdraw_amount", [
    ("12345", 50),
    ("67890", 150)
])
def test_withdraw(account_number, withdraw_amount):
    response = requests.post(f"{BASE_URL}/{account_number}/withdraw", json={"amount": withdraw_amount})
    assert response.status_code == 200
    data = response.json()
    assert data["account_number"] == account_number
    assert data["new_balance"] >= 0

@pytest.mark.parametrize("withdraw_amount", [100000, 1000000])
def test_overdraft(withdraw_amount):
    response = requests.post(f"{BASE_URL}/12345/withdraw", json={"amount": withdraw_amount})
    assert response.status_code in [400, 200]
    data = response.json()
    assert "error" in data

@pytest.mark.parametrize("invalid_account", ["99999", "00000", "abcde"])
def test_invalid_account(invalid_account):
    response = requests.get(f"{BASE_URL}/{invalid_account}/balance")
    assert response.status_code in [400, 404]
    data = response.json()
    assert "error" in data

@pytest.mark.parametrize("invalid_amount", [0, -50, -1])
def test_deposit_invalid_amount(invalid_amount):
    response = requests.post(f"{BASE_URL}/12345/deposit", json={"amount": invalid_amount})
    assert response.status_code == 400
    data = response.json()
    assert "error" in data

@pytest.mark.parametrize("invalid_amount", [0, -100])
def test_withdraw_invalid_amount(invalid_amount):
    response = requests.post(f"{BASE_URL}/12345/withdraw", json={"amount": invalid_amount})
    assert response.status_code == 400
    data = response.json()
    assert "error" in data
