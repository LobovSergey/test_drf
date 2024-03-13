FROM python:latest
WORKDIR /django_test
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN python /django_test/core/manage.py makemigrations && python /django_test/core/manage.py migrate
EXPOSE 8000
CMD ["python", "/django_test/core/manage.py", "runserver"]