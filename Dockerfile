FROM python:3.10.8

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --upgrade pip
RUN pip install fastapi
RUN pip install uvicorn["standard"]
RUN pip install pandas
RUN pip install lxml
RUN pip install pymongo

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--port", "8000"]
