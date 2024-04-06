FROM python: 3.11-slim

COPY . .

RUN pip install -r requirements.txt

CDM ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]