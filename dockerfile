FROM python:3.9

RUN mkdir /minibank

WORKDIR /minibank

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x /minibank/docker/*.sh

#RUN alembic upgrade head

CMD [ "gunicorn", "app.main:app", "--workers", "1", "--worker-class","uvicorn.workers.UvicornWorker", "--bind=0.0.0.0:8000"]

