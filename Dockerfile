FROM python:3.7.0-stretch
RUN useradd -m fbot
WORKDIR /home/fbot
COPY requirements.txt /home/fbot
COPY main.py /home/fbot
COPY config.cfg /home/fbot
RUN pip install -r requirements.txt
USER fbot
CMD python main.py