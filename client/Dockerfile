FROM node:18-alpine AS build

WORKDIR /app

COPY . .


RUN npm install -g @quasar/cli
RUN npm install


CMD ["npx", "quasar", "dev"]
