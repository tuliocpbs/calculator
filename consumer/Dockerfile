FROM python:3.7-alpine

WORKDIR /app

COPY . .

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install -r requirements/requirements-prd.txt

CMD ["python", "run.py"]