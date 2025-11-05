# Use Node base image
FROM node:18-alpine

WORKDIR /app

# Copy package files and install dependencies
COPY package*.json ./
RUN npm install

# Copy frontend files
COPY . .

# Expose frontend port
EXPOSE 3000

# Run app
CMD ["npm", "start"]
