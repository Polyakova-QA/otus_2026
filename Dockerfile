FROM python:3.12-slim-bookworm

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    HEADLESS=1

WORKDIR /work

RUN apt-get update && apt-get install -y --no-install-recommends \
        wget \
        gnupg \
        ca-certificates \
        firefox-esr \
    && wget -qO- https://dl.google.com/linux/linux_signing_key.pub \
        | gpg --dearmor -o /usr/share/keyrings/google-chrome.gpg \
    && echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google-chrome.gpg] \
        http://dl.google.com/linux/chrome/deb/ stable main" \
        > /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update && apt-get install -y --no-install-recommends \
        google-chrome-stable \
    && ln -sf /usr/bin/firefox-esr /usr/bin/firefox \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /work/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /work/

ENTRYPOINT ["pytest", "tests"]
CMD ["--browser", "chrome"]