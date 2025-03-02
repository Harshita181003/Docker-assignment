# Use a lightweight base image
FROM python:3.9-slim

# Set working directory
WORKDIR /home/app

# Copy script and data folder into the container
COPY scripts/script.py /home/app/script.py
COPY data /home/data

# Install dependencies (if needed)
RUN pip install --no-cache-dir --upgrade pip

# Run script when container starts
CMD ["python", "/home/app/script.py"]
 
