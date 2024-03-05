FROM python:3.10.11
ENV PYTHONUNBUFFERED 1
WORKDIR /django_test_stripe
COPY requirements.txt /django_test_stripe/
RUN pip install -r requirements.txt
COPY . /django_test_stripe/