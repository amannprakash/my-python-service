FROM python:3.12-slim
WORKDIR /app
# Install dependencies
RUN pip install flask  # Add your requirements here
COPY app.py .
# Run the application
CMD ["python", "app.py"]