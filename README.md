# ATM System

## Project Description

A simple ATM system implemented in Python using Flask. It allows users to check balance, deposit money, and withdraw money via a RESTful API.

## Features

1. **Check Balance** – Retrieve the current balance using an account number.
2. **Deposit Money** – Add a specified amount to the account balance.
3. **Withdraw Money** – Withdraw a specified amount if sufficient funds are available.

Accounts are stored in memory as a Python dictionary.

## GitHub Repository

[https://github.com/AdanShamma/atm-system](https://github.com/AdanShamma/atm-system)

## Live API URL

[https://web-production-ec481.up.railway.app/](https://web-production-ec481.up.railway.app/)

## API Endpoints Overview

* `/accounts/<account_number>/balance` – GET current balance
* `/accounts/<account_number>/deposit` – POST deposit amount
* `/accounts/<account_number>/withdraw` – POST withdraw amount

---

## Example Commands & Responses

### Account `12345`

**Check Balance:**

```powershell
Invoke-RestMethod -Uri "https://web-production-ec481.up.railway.app/accounts/12345/balance" -Method GET
```

**Response:**

```json
{
  "account_number": "12345",
  "balance": 600.0
}
```

**Deposit Money:**

```powershell
Invoke-RestMethod -Uri "https://web-production-ec481.up.railway.app/accounts/12345/deposit" `
    -Method POST `
    -ContentType "application/json" `
    -Body '{"amount":200}'
```

**Response:**

```json
{
  "account_number": "12345",
  "new_balance": 800.0
}
```

**Withdraw Money:**

```powershell
Invoke-RestMethod -Uri "https://web-production-ec481.up.railway.app/accounts/12345/withdraw" `
    -Method POST `
    -ContentType "application/json" `
    -Body '{"amount":100}'
```

**Response:**

```json
{
  "account_number": "12345",
  "new_balance": 700.0
}
```

### Account `67890`

**Check Balance:**

```powershell
Invoke-RestMethod -Uri "https://web-production-ec481.up.railway.app/accounts/67890/balance" -Method GET
```

**Response:**

```json
{
  "account_number": "67890",
  "balance": 1000.0
}
```

**Deposit Money:**

```powershell
Invoke-RestMethod -Uri "https://web-production-ec481.up.railway.app/accounts/67890/deposit" `
    -Method POST `
    -ContentType "application/json" `
    -Body '{"amount":300}'
```

**Response:**

```json
{
  "account_number": "67890",
  "new_balance": 1300.0
}
```

**Withdraw Money:**

```powershell
Invoke-RestMethod -Uri "https://web-production-ec481.up.railway.app/accounts/67890/withdraw" `
    -Method POST `
    -ContentType "application/json" `
    -Body '{"amount":500}'
```

**Response:**

```json
{
  "account_number": "67890",
  "new_balance": 800.0
}
```

---

## Error Handling Examples

**Withdraw More Than Balance:**

```powershell
Invoke-RestMethod -Uri "https://web-production-ec481.up.railway.app/accounts/12345/withdraw" `
    -Method POST `
    -ContentType "application/json" `
    -Body '{"amount":1000}'
```

**Response:**

```json
{
  "error": "Insufficient funds"
}
```

**Invalid Account Number:**

```powershell
Invoke-RestMethod -Uri "https://web-production-ec481.up.railway.app/accounts/99999/balance" -Method GET
```

**Response:**

```json
{
  "error": "Account not found"
}
```

---

## Demo Flow:

1. Check balance of `12345` : see 500.
2. Deposit 200 : new balance 700.
3. Withdraw 100: new balance 600.
4. Check balance: confirm 600.
5. Try to withdraw 1000: error `Insufficient funds`.
6. Check balance of invalid account `99999`: error `Account not found`.

---

## Notes / Assumptions:
1. Server-side only no frontend.
2. Accounts are in memory and reset on server restart.
3. Example accounts: `12345` with 500, `67890` with 1000.
4. Error handling included for insufficient funds, negative amounts, and invalid accounts.
