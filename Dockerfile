FROM python

WORKDIR /media_devops
COPY media_devops.py .

RUN pip install -r requirements.txt

CMD [ "python", "media_devops.py" ]