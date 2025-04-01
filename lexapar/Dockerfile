# Use the official Python image as the base
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the application files to the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the default port 8000
EXPOSE 8000

# ENTRYPOINT ["/entrypoint.sh"]
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]