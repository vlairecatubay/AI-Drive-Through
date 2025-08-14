\
    @echo off
    python -m venv .venv
    call .venv\Scripts\activate
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    python - <<PY
import nltk
nltk.download('punkt'); nltk.download('stopwords')
print('nltk downloads complete')
PY
    echo Setup complete. Run: .venv\Scripts\activate
