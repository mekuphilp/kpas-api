FROM ubuntu:18.04
RUN groupadd -g 999 appuser && useradd -r -u 999 -g appuser appuser && mkdir /home/app && apt update && apt install python3 python3-pip python3-venv -y && /usr/bin/python3 -m venv /app/venv
COPY __main__.py main.py requirements.txt ca.crt /app/
COPY src /app/src/
RUN /app/venv/bin/python3 -m pip install -r /app/requirements.txt && chown appuser:appuser -R /home/app
USER appuser
WORKDIR /app/
ENV PYTHONPATH="/app"
CMD ["./venv/bin/python3", "__main__.py"]
