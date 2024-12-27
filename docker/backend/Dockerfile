FROM python:3.12

WORKDIR /srv/app

ENV PATH="${PATH}:/root/.local/bin"
ENV PYTHONPATH=.

COPY requirements.txt .
RUN pip install --upgrade pip
#RUN curl https://sh.rustup.rs -sSf -y | sh
#RUN export PATH="$HOME/.cargo/bin:$PATH"
RUN pip install -r requirements.txt

# for migrations
COPY migrations .
COPY pyproject.toml .

COPY src/ .