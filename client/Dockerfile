FROM node:18-alpine AS build

WORKDIR /app

COPY package*.json ./


RUN npm install -g @quasar/cli
RUN npm install


COPY . .

RUN quasar build

FROM nginx:alpine

COPY --from=build /app/dist/spa /usr/share/nginx/html


EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
