from django.test import TestCase

curl \ 12
  -X POST \ http://127.0.0.1:8000/
  -H "Content-Type: application/json" \
  -d '{"username": "davidattenborough", "password": "boatymcboatface"}' \
  http://localhost:8000/api/token/
