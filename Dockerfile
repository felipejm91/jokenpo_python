FROM python:3.10.4-slim-buster
WORKDIR /app
COPY . .
CMD [ "python3", "-m", "jokenpo.py","run" ]
