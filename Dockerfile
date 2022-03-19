FROM python:3.9
WORKDIR /app
COPY . .
EXPOSE 7800
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python", "test.py"]