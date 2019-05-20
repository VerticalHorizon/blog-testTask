FROM python:3.7-alpine

RUN apk update && \
 apk add libpq postgresql-dev build-base && \
 apk add --no-cache git openssh && \
 apk add --virtual .build-deps gcc musl-dev && \
 apk --purge del .build-deps

WORKDIR /opt/application
VOLUME ./app /opt/application
COPY Pipfile /opt/application/Pipfile
COPY Pipfile.lock /opt/application/Pipfile.lock
RUN pip install -U pip && pip install pipenv && pipenv install --system --deploy

ENV PYTHONPATH=/opt/application

COPY bin/entrypoint.sh /entrypoint/entrypoint.sh
RUN chmod -R 755 /entrypoint/
ENV PATH /entrypoint:$PATH

CMD ["/entrypoint/entrypoint.sh"]
