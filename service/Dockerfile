FROM python:3

WORKDIR /usr/src/app
EXPOSE 8000
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "./manage.py", "runserver", "0.0.0.0:8000" ]
