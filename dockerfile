FROM python:3.10

# RUN ["apt-get", "update"]
# RUN ["apt-get", "-y", "install", "vim"]

WORKDIR /app

COPY . .

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6 -y
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5001

CMD python ./main.py