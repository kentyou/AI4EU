FROM python:3.8

# Move to a directory inside the image
WORKDIR /opt
COPY main.py .
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Move a directory where we will execute the script
RUN mkdir /opt/run
WORKDIR /opt/run

ENTRYPOINT ["python","/opt/main.py"]
