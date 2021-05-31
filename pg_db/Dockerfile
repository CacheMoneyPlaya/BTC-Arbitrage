FROM postgres:latest

RUN apt-get update && apt-get install -y build-essential \
    vim \

 && apt-get clean \
 && apt-get autoremove \
 && rm -rf /var/lib/apt/lists/*

COPY .pgpass ./home

RUN chmod 0600 home/.pgpass

EXPOSE 5432/tcp

CMD ["/bin/bash"]
