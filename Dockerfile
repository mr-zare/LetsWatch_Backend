# Use an official Python runtime as a parent image
FROM python:3.11

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set the working directory to /app
WORKDIR /app

# Create a virtual environment and activate it
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Activate the virtual environment
RUN . /opt/venv/bin/activate

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Expose port 8000 to the outside world
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]