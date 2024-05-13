FROM python:3.12

WORKDIR /code

ADD ./requirements.txt /code/requirements.txt

RUN pip install -r /code/requirements.txt

COPY . /code

CMD ["python", "main.py"]