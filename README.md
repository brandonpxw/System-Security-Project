# System Security Project: Securing a Car Dealership Web App

My [Year 1 car dealership web app](https://github.com/brandonpxw/App-Development-Project), rebuilt with a SQL database and security features that address
the OWASP Top 10 web application risks.

**Nanyang Polytechnic · Year 2 · 2022** · [Portfolio page](https://brandonpxw.github.io/portfolioPages/sysecproject.html)

## Security features

| Area | What's in it |
|---|---|
| Logging in | reCAPTCHA, two-factor authentication, rate limiting, password complexity rules |
| Accounts | Password recovery, login history, login by region, IP address and device tracking |
| Requests | CSRF protection, input validation, path traversal prevention |
| Data | Encryption and data protection, session management (30-minute sessions) |
| Monitoring | Audit logs |

It keeps the original shop features: shopping cart, car and accessory inventory, user and admin
accounts, feedback and reviews, car services and reward points.

## Built with

Python · Flask · MySQL · WTForms · Flask-Mail · reCAPTCHA · Fernet encryption

## Running it

1. Install the packages: `pip install -r requirements.txt`. If a module imported in
   `__init__.py` is still missing, install it with `pip install <module name>`.
2. In MySQL Workbench, create a schema named `pythonlogin` and run `database.sql`.
3. Set your own credentials as environment variables (they're no longer stored in the code):
   `SECRET_KEY`, `MYSQL_USER`, `MYSQL_PASSWORD`, `MAIL_USERNAME`, `MAIL_PASSWORD`,
   `RECAPTCHA_PUBLIC_KEY` and `RECAPTCHA_PRIVATE_KEY`. The encryption key (`symmetric.key`) is
   created automatically when the first account registers.
4. Run `python __init__.py`.

The page templates (HTML) aren't included in this repository, so the app won't display pages
until they're added. For the default admin account, contact me.

## What I learned

This project built on one I did in Year 1. Besides improving its design and features, I moved
its data into a SQL database and added security features aimed at the OWASP Top 10
vulnerabilities.
