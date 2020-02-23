FROM python:3.7-alpine

WORKDIR /app

COPY . .

RUN pip install -r requirements/requirements-prd.txt

EXPOSE 80
CMD ["gunicorn","-c","gconfig.py","src.app:app"]