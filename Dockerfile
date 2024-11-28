# Use the official Python image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Copy project files to the working directory
COPY . /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the application port
EXPOSE 8000

# Start the Django app using Gunicorn
CMD ["gunicorn", "mainpaper.wsgi:application", "--bind", "0.0.0.0:8000"]