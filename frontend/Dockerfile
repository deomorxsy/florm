# Use the official Node.js image as a base image
FROM node:14-alpine

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY package.json package-lock.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Expose port 5173 || 3000
EXPOSE 5173

# Command to start the development server
CMD ["npm", "run", "dev"]

