FROM python:3.10
COPY . /apollo
WORKDIR /apollo
RUN pip install -r requirements.txt
CMD ["python3", "Apollo.py"]

