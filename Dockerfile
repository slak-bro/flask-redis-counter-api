FROM python:3.7
RUN pip install pipenv
WORKDIR /app
COPY Pipfile .
RUN pipenv lock
RUN pipenv install --system --deploy
COPY counterapi/ /app
EXPOSE 8080
CMD pipenv run gunicorn -b 0.0.0.0:8080 api:app