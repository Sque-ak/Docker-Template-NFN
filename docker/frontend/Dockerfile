FROM node:lts-alpine

WORKDIR /srv/app

ENV PATH /srv/app/node_modules/.bin:$PATH

COPY package*.json ./
RUN npm install
COPY . .

EXPOSE 3000
RUN npm run build