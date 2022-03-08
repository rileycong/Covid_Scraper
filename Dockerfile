FROM python:3.9-alpine
WORKDIR /app
COPY . .
EXPOSE 7800
RUN pip install --upgrade pip
RUN apk add --update --no-cache g++ gcc libxslt-dev
RUN pip install -r requirements.txt
ENTRYPOINT ['python', 'scrape.py']