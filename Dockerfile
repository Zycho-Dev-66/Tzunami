FROM python:3.9.7-slim-buster
RUN apt-get update && apt-get upgrade -y
RUN python3.9 -m pip install -U pip
RUN python3.9 -m pip install -r requirements.txt
CMD python app.py
