FROM alpine:lastest
LABEL Description="Ontario Emergency App build env"

RUN apk update && apk upgrade && \
    apk add python3 python3-pip pyhton3-tk && \
    pip3 install pyinstaller --break-system-packages && \
    cd $HOME && git clone https://github.com/AFOEK/OEApp && \
    cd OEApp && pip3 install -r requirements.txt && \
    pyinstaller --onefile OEApp.py