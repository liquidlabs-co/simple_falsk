FROM python:3.5
RUN mkdir /simple_flask
WORKDIR /simple_flask
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
