FROM python:3.8

RUN apt-get update && apt-get install -y build-essential \
    python3-pip \
    vim \
    cron \

 && apt-get clean \
 && apt-get autoremove \
 && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

WORKDIR ./root/arbitrage_opp

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD tail -f /dev/null
