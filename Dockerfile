
FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


COPY ./requirements.txt /tmp/requirements.pip
RUN pip install -r /tmp/requirements.pip

WORKDIR /srv/libs
COPY ./ ./

ENV PATH="/srv/bin:${PATH}"
ENV PYTHONPATH="/srv/libs"

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
