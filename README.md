# AI-Drive-Through

AI-Drive-Through is an AI-powered drive-through ordering system with a Python backend and a web-based frontend.

## Project Structure

```
AI-Drive-Through/
├── backend/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app/
│       ├── __init__.py
│       ├── main.py
│       ├── models/
│       ├── routers/
│       ├── services/
│       └── utils/
└── frontend/
    └── drive_thru_ui/
        ├── index.html
        ├── css/
        │   └── style.css
        └── js/
            ├── api.js
            └── app.js
```

## Backend

- **Location:** `backend/`
- **Tech:** Python (FastAPI or Flask recommended)
- **Features:** Handles ASR, NLU, menu, orders, and kitchen services.

### Setup

```sh
cd backend
pip install -r requirements.txt
python app/main.py
```

Or with Docker:

```sh
cd backend
docker build -t ai-drive-through-backend .
docker run -p 8000:8000 ai-drive-through-backend
```

## Frontend

- **Location:** `frontend/drive_thru_ui/`
- **Tech:** HTML, CSS, JavaScript
- **Features:** User interface for placing and managing orders.

### Setup

Open `frontend/drive_thru_ui/index.html` in your browser.

## Contributing

Pull requests are welcome. For major changes, please open an issue first.

## License

MIT License

---

Feel free to update this README with more details
