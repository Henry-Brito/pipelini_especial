FROM python

WORKDIR /media_devops
COPY media_devops.py .

CMD [ "python", "media_devops.py" ]