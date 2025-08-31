# Use a slim Python runtime as a parent image
FROM python:3.12-slim

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and switch to a non-root user for security
RUN useradd -m -u 1000 user
USER user

# Set the working directory
WORKDIR /home/user/app
ENV PATH="/home/user/.local/bin:${PATH}"

# Copy and install dependencies
COPY --chown=user requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the application code
COPY --chown=user . .

# Copy and set permissions for entrypoint script
COPY --chown=user entrypoint.sh .
RUN chmod +x entrypoint.sh

# Run collectstatic to gather all static files
RUN python manage.py collectstatic --no-input

# Expose the port the app runs on
EXPOSE 7860

# Run the entrypoint script
CMD ["/home/user/app/entrypoint.sh"]