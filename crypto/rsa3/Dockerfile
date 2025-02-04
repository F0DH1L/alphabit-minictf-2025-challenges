FROM python:3.12


RUN apt update && apt install -y socat
# Install required dependencies
RUN pip install pycryptodome

# Set the working directory
WORKDIR /app

# Copy the script into the container
COPY challenge /app

# Set script permissions
RUN chmod +x entrypoint.sh
RUN chmod +x chall.py

# Define the entrypoint
CMD ["./entrypoint.sh"]