# CampusFind - Smart Campus Lost & Found

## 1. XAMPP
Start Apache and MySQL in XAMPP.

Open phpMyAdmin and create:
`smart_campus_lost_found`

You can also import `database/schema.sql`.

## 2. Python environment
Create a PyCharm virtual environment, then:

```bash
pip install -r requirements.txt
```

## 3. Environment
Copy `.env.example` to `.env`.

Default XAMPP MySQL settings:
- user: root
- password: empty
- host: 127.0.0.1
- port: 3306

If you set a MySQL password, put it in `.env`.

## 4. Run
```bash
python app.py
```

Open:
http://127.0.0.1:5000

## 5. Make an admin
Register a normal account first. Then in phpMyAdmin:

```sql
UPDATE users
SET role = 'admin'
WHERE email = 'your-email@example.com';
```

Then log out and log back in.

## Notes
- Uploaded item images go to `static/uploads/lost` and `static/uploads/found`.
- Passwords are hashed.
- Claims require an ownership description and admin approval.
- The included matching system is a rule-based prototype. AI/image similarity can be added as the next phase.
