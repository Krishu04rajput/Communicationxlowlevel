# CommunicationX — Local SQLite Edition

This version is intentionally self-contained for development with friends.

## Run

1. Install Python 3.10+.
2. Open this folder in Terminal.
3. Run:

```bash
python -m pip install -r requirements.txt
python run_local.py
```

4. Open `http://127.0.0.1:5000`.

The app automatically creates `communicationx.db` beside the code. No Vercel, Render, Supabase, Neon, PostgreSQL, or `DATABASE_URL` is required.

## Database

SQLite is used by default. The database is a single local file:

`communicationx.db`

Back it up by copying that file. Do not commit it to a public GitHub repository if it contains real users/messages.

## Notes

This is the simple local/private setup. It is not intended as a production public-internet deployment.
