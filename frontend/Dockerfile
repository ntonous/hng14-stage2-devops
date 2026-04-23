FROM node:20-alpine

WORKDIR /app

RUN addgroup -S appgroup && adduser -S appuser -G appgroup

COPY package*.json ./
RUN npm install --omit=dev

COPY . .

USER appuser

EXPOSE 3000

HEALTHCHECK CMD wget --spider -q http://localhost:3000/health || exit 1

CMD ["npm", "start"]