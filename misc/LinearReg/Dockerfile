# Use a minimal Python image
FROM python:3.12

# Create a non-root user for security
RUN useradd -m chal_user

# Set working directory and switch to the non-root user
WORKDIR /home/chal_user
USER chal_user

# Copy challenge files
COPY challenge/app.py . 

# Install dependencies
RUN pip install --no-cache-dir numpy

# Expose port for the challenge
EXPOSE 1337

# Run the challenge
CMD ["python", "app.py"]
