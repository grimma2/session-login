# Use an official Python runtime as a base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /anallogin

COPY requirements.txt /anallogin/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /anallogin/

# Run migrations and collect static files if needed (replace with your actual commands)
RUN python manage.py migrate

# Expose the port the app runs on
EXPOSE 8000

# Define the command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]