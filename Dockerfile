FROM python:3.10.5-slim-bullseye

WORKDIR /code

COPY ./ ./

RUN pip install -U pip &&  \
    pip install -r requirements.txt

WORKDIR /code/src

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]