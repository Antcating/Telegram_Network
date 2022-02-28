
    FROM mongo:5.0.2

    USER root

    WORKDIR /home

    RUN apt-get update -y
    RUN apt install -y python3 python3-pip git

    # clone from git
    RUN git clone https://github.com/AndrewHaluza/telegram_report_bot_ua.git 

    WORKDIR /home/telegram_report_bot_ua

    # make build locally
    # COPY ./ ./
    
    COPY ./docker-entrypoint.sh ./docker-entrypoint.sh

    RUN pip3 install -r ./requirements.txt

    RUN chmod +x ./docker-entrypoint.sh

    ENTRYPOINT [ "./docker-entrypoint.sh" ]