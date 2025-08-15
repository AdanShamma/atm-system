**# ATM System**



\## Project Description

A simple ATM system implemented in Python using Flask. It allows users to check balance, deposit money, and withdraw money.



\## Features

1.Check balance– Retrieve current balance using account number.

2\.Deposit money – Add a specified amount to the account balance.

3\.Withdraw money– Withdraw a specified amount if sufficient funds are available.



Accounts are stored in memory as a Python dictionary.



\## GitHub Repository

\[https://github.com/AdanShamma/atm-system](https://github.com/AdanShamma/atm-system)



\## Live API URL

\[https://web-production-ec481.up.railway.app/](https://web-production-ec481.up.railway.app/)



\## API Endpoints Overview

\* `/accounts/<account\_number>/balance` – GET current balance

\* `/accounts/<account\_number>/deposit` – POST deposit amount

\* `/accounts/<account\_number>/withdraw` – POST withdraw amount



---------------------------------------------------------------------------------------



\## Example Commands \& Responses



**### Account `12345`**



1\.Check balance:

```powershell

Invoke-RestMethod -Uri "https://web-production-ec481.up.railway.app/accounts/12345/balance" -Method GET

```

\*Response:\*

```json

{

&nbsp; "account\_number": "12345",

&nbsp; "balance": 600.0

}

```

2\.Deposit money:

```powershell

Invoke-RestMethod -Uri "https://web-production-ec481.up.railway.app/accounts/12345/deposit" `

&nbsp;   -Method POST `

&nbsp;   -ContentType "application/json" `

&nbsp;   -Body '{"amount":200}'

```



\*Response:\*

```json

{

&nbsp; "account\_number": "12345",

&nbsp; "new\_balance": 800.0

}

```

3\.Withdraw money:

```powershell

Invoke-RestMethod -Uri "https://web-production-ec481.up.railway.app/accounts/12345/withdraw" `

&nbsp;   -Method POST `

&nbsp;   -ContentType "application/json" `

&nbsp;   -Body '{"amount":100}'

```

\*Response:\*



```json

{

&nbsp; "account\_number": "12345",

&nbsp; "new\_balance": 700.0

}

```



**### Account `67890`**



1\.Check balance:

```powershell

Invoke-RestMethod -Uri "https://web-production-ec481.up.railway.app/accounts/67890/balance" -Method GET

```

\*Response:\*

```json

{

&nbsp; "account\_number": "67890",

&nbsp; "balance": 1000.0

}

```



2\.Deposit money:

```powershell

Invoke-RestMethod -Uri "https://web-production-ec481.up.railway.app/accounts/67890/deposit" `

&nbsp;   -Method POST `

&nbsp;   -ContentType "application/json" `

&nbsp;   -Body '{"amount":300}'

```

\*Response:\*

```json

{

&nbsp; "account\_number": "67890",

&nbsp; "new\_balance": 1300.0

}

```



3\.Withdraw money:

```powershell

Invoke-RestMethod -Uri "https://web-production-ec481.up.railway.app/accounts/67890/withdraw" `

&nbsp;   -Method POST `

&nbsp;   -ContentType "application/json" `

&nbsp;   -Body '{"amount":500}'

```

\*Response:\*



```json

{

&nbsp; "account\_number": "67890",

&nbsp; "new\_balance": 800.0

}

```



---------------------------------------------------------------------------------------------



\## Error Handling Examples



1\. Withdraw more than balance:

```powershell

Invoke-RestMethod -Uri "https://web-production-ec481.up.railway.app/accounts/12345/withdraw" `

&nbsp;   -Method POST `

&nbsp;   -ContentType "application/json" `

&nbsp;   -Body '{"amount":1000}'

```



\*Response:\*

```json

{

&nbsp; "error": "Insufficient funds"

}

```



2\.Invalid account number:



```powershell

Invoke-RestMethod -Uri "https://web-production-ec481.up.railway.app/accounts/99999/balance" -Method GET

```



\*Response:\*



```json

{

&nbsp; "error": "Account not found"

}

```



----------------------------------------------------



\## Demo Flow

1\. Check balance of `12345` → see 500.

2\. Deposit 200 → new balance 700.

3\. Withdraw 100 → new balance 600.

4\. Check balance → confirm 600.

5\. Try to withdraw 1000 → error `Insufficient funds`.

6\. Check balance of invalid account `99999` → error `Account not found`.



------------------------------------------------



\## Notes / Assumptions

1. Server side only no frontend.
2. Accounts are in memory and  data resets on server restart.
3. Example accounts: `12345` with 500, `67890` with 1000.
4. Error handling included for insufficient funds, negative amounts, and invalid accounts.



