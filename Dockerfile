FROM python:3.10.11
ENV PYTHONUNBUFFERED 1
EXPOSE 8000
WORKDIR /django_test_stripe
ADD . /django_test_stripe
RUN pip install -r requirements.txt
