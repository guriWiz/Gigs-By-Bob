FROM python:3.12-alpine

# Set the timezone to Asia/Kolkata
RUN apk add --no-cache tzdata

ENV TZ=Asia/Kolkata
RUN cp /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /app
COPY . .

# Install pip requirements
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

# Run bot
CMD ["python", "bot.py"]