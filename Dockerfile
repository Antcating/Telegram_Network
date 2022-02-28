
    FROM ubuntu

    USER root

    RUN apt update -y
    RUN apt install -y python3 python3-pip git

    WORKDIR /home

    RUN git clone https://github.com/AndrewHaluza/telegram_report_bot_ua.git 

    WORKDIR /home/telegram_report_bot_ua

    COPY ./.env ./

    RUN pip3 install -r ./requirements.txt

    CMD python3 ./main.py