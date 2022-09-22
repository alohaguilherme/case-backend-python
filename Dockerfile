FROM python:3.10.6

RUN apt update && apt install -y --no-install-recommends 
RUN apt-get install -y build-essential
RUN pip install --upgrade pip
RUN pip install pdm 


WORKDIR /app
COPY . .
ENV PORT=$PORT
ENV MY_PYTHON_PACKAGES=/app/__pypackages__/3.10
ENV PYTHONPATH=${PYTHONPATH}/app/src
ENV PATH $PATH:${MY_PYTHON_PACKAGES}/bin
ENV PYTHONDONTWRITEBYTECODE=1

RUN echo 'eval "$(pdm --pep582)"' >> ~/.bashrc

EXPOSE $PORT

RUN pdm install --production -v
RUN pdm sync

CMD ["pdm", "run", "uwsgi", "--ini", "wsgi.ini"]