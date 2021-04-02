FROM python:3.9-slim

ENV PYTHONUNBUFFERED=1
ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN mkdir /home/app 

RUN python3 -m pip install --no-cache-dir geoip2 flask

COPY ./python/app.py /home/app/ 
COPY ./html /home/app
COPY ./GeoLite2-City.mmdb /home/app
EXPOSE 8080

WORKDIR "/home/app/"
CMD ["python3", "/home/app/app.py"]

