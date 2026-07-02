FROM python:3.10-slim

# Set working directory
WORKDIR /code

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the rest of the application files
COPY . .

# Run the application (Hugging Face Spaces uses port 7860 by default)
CMD ["gunicorn", "-b", "0.0.0.0:7860", "app:app"]
