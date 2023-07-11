# Use a specific Python base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN python -m venv venv
RUN venv/bin/pip install --no-cache-dir --upgrade pip
RUN venv/bin/pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

# Expose the necessary port
EXPOSE 5000

# Specify the command to run the service
CMD ["venv/bin/python", "service.py"]
