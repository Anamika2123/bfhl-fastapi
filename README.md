# BFHL FastAPI

Python FastAPI implementation of the BFHL `/bfhl` POST endpoint.

## What it does
- Accepts JSON: `{ "data": ["a","1","334","4","R","$"] }`
- Returns:
  - `is_success`
  - `user_id` as `{full_name_ddmmyyyy}` in lowercase with underscores
  - `email`
  - `roll_number`
  - `odd_numbers` (strings)
  - `even_numbers` (strings)
  - `alphabets` (each alphabetic token uppercased)
  - `special_characters`
  - `sum` of numeric tokens (string)
  - `concat_string`: all alphabetic **characters** across input, reversed, alternating caps

## Local run
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
export FULL_NAME="John Doe"
export DOB_DDMMYYYY="17091999"
export EMAIL_ID="john@xyz.com"
export ROLL_NUMBER="ABCD123"
uvicorn main:app --host 0.0.0.0 --port 8000
```

Test:
```bash
curl -s -X POST http://127.0.0.1:8000/bfhl   -H "Content-Type: application/json"   -d '{"data":["a","1","334","4","R","$"]}' | jq
```

## Deploy to Render (recommended)
1. Push this folder to a **public GitHub repo**.
2. Create a new **Web Service** on Render from your repo.
3. Use these settings if not auto-detected:
   - Runtime: **Python**
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn -k uvicorn.workers.UvicornWorker main:app`
4. Add Environment Variables:
   - `FULL_NAME` e.g. `Anamika Unnikrishnan`
   - `DOB_DDMMYYYY` e.g. `17091999`
   - `EMAIL_ID` e.g. `your@vitstudent.ac.in`
   - `ROLL_NUMBER` e.g. `22BCE0000`
5. Wait for deploy to finish. Your endpoint will be:
   - `POST https://<your-app>.onrender.com/bfhl`

## Examples
Request
```json
{"data":["a","1","334","4","R","$"]}
```
Response (shape example)
```json
{
  "is_success": true,
  "user_id": "john_doe_17091999",
  "email": "john@xyz.com",
  "roll_number": "ABCD123",
  "odd_numbers": ["1"],
  "even_numbers": ["334","4"],
  "alphabets": ["A","R"],
  "special_characters": ["$"],
  "sum": "339",
  "concat_string": "Ra"
}
```
