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
<<<<<<< HEAD
=======

## Approach

The goal was to create a simple, lightweight ATM API that lets users check their balance, deposit money, and withdraw money via HTTP requests.
I kept the implementation minimal and direct, storing accounts in a Python dictionary right inside the application for instant lookups and updates.
Using Flask allowed me to quickly expose these operations as REST endpoints (GET for checking balance, POST for deposits/withdrawals) in a way that’s easy to understand, test, and extend.
Because this is a demonstration project, I prioritized simplicity over persistence. That’s why balances reset when the server restarts — no external database or file storage is required.

## Design Decisions

* **Flask**: chosen for speed of development and simplicity for REST APIs.
* **In-memory storage**: avoids complexity and is perfect for a demo resets on server restart.
* **Clear endpoint structure**: `/accounts/<account_number>/balance`, `/deposit`, `/withdraw` for clarity.
* **Error handling**: Explicit checks for invalid accounts, insufficient funds, and invalid amounts.
* **Modular code**: account operations handled separately from route definitions.

## Challenges Faced

* **Persistence trade-off**: Storing data in memory made the app simple, but it means balances are lost on restart. For production, a database would be essential.
* **Testing**:Ensuring tests worked without relying on an external data file meant setting up predictable in-memory accounts for test runs.
* **Deployment**: Configuring Railway deployment required making sure Flask listened on the correct port and had the right Procfile setup.
* **Error responses**: Needed to ensure all error cases returned JSON instead of default HTML error pages so clients can handle them properly.

## API Execution Instructions

### Using `curl`

**Check Balance:**

```bash
curl -X GET https://web-production-ec481.up.railway.app/accounts/12345/balance
```

**Deposit:**

```bash
curl -X POST https://web-production-ec481.up.railway.app/accounts/12345/deposit \
     -H "Content-Type: application/json" \
     -d '{"amount":200}'
```

**Withdraw:**

```bash
curl -X POST https://web-production-ec481.up.railway.app/accounts/12345/withdraw \
     -H "Content-Type: application/json" \
     -d '{"amount":100}'
```

### Using Postman

1. Open Postman.
2. Set the request method to `GET` or `POST` depending on the operation.
3. Enter the full API URL.
4. For `POST` requests, go to **Body → raw → JSON** and enter:

```json
{
  "amount": 200
}
```

5. Send the request and view the JSON response.
>>>>>>> 2d49578 (Update README and add test files)
