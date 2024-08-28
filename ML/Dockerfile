# Use an official Python runtime as the base image
FROM python:3.11

# Set the working directory in the container
WORKDIR /code

# Copy the requirements file to the working directory
COPY ./requirements.txt /code/requirements.txt

# Install the required dependencies
RUN pip install --no-cache-dir -r /code/requirements.txt

# Copy the rest of the application code to the working directory
COPY ./app /code/app

EXPOSE 8000

# Specify the command to run when the container starts
CMD [ "uvicorn", "app.server:app", "--host", "0.0.0.0", "--port", "8000" ]