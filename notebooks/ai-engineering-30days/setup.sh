#!/usr/bin/env bash
set -e
python3 -m venv .venv
. .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python - <<'PY'
import nltk
nltk.download('punkt'); nltk.download('stopwords')
print('nltk downloads complete')
PY
echo "Setup complete. Activate venv with: . .venv/bin/activate"
