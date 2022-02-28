
    FROM ubuntu

    USER root

    RUN apt update -y
    RUN apt install -y python3 python3-pip git

    WORKDIR /home

    # clone from git
    RUN git clone https://github.com/AndrewHaluza/telegram_report_bot_ua.git 

    WORKDIR /home/telegram_report_bot_ua

    # make build locally
    # COPY ./ ./

    RUN pip3 install -r ./requirements.txt

    ENTRYPOINT [ "python3", "./main.py" ]