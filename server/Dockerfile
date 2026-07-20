# 1. Add a base image (Python 3.12 slim bookworm)
FROM python:3.12.0-slim-bookworm

# Environment variables for optimal Python container execution
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV APP=/app

# 2. Change the working directory
WORKDIR $APP

# 3. Add the requirements.txt file
COPY requirements.txt $APP

# 4. Install and update Python package manager, then install your application packages
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt

# Copy the rest of your local repository development files into the container
COPY . $APP

# 5. Expose port
EXPOSE 8000

# Fix execution permissions on your entrypoint runner file script
RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/bin/bash", "/app/entrypoint.sh"]

# 6. Run the command to start the application using Gunicorn production workers
CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "djangoproj.wsgi"]
