FROM python:3.9.10-bullseye AS builder
ADD ./requirements.txt /app/

# Set timezone
RUN apt update; apt -y install tzdata && \
cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

## Install Python packages
WORKDIR /app
RUN pip install -r requirements.txt

FROM python:3.9.10-bullseye AS runner

RUN apt update && apt -y install busybox-static

# Copy dependencies from builder / Set timezone
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /etc/localtime /etc/localtime

# Add script to crontab
RUN mkdir -p /var/spool/cron/crontabs/ && \
    echo '0 7 * * * cd /app; python run.py' >> /var/spool/cron/crontabs/root

# Load app
ADD ./ /app

# Run crond
ENTRYPOINT ["busybox", "crond", "-f", "-L", "/dev/stderr"]
