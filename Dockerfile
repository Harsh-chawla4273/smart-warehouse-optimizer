# Use Python 3.9 image
FROM python:3.9

# Set working directory
WORKDIR /code

# Install dependencies
RUN pip install --no-cache-dir streamlit pandas plotly numpy

# Copy all files to the container
COPY . .

# Expose Streamlit's default port
EXPOSE 7860

# Command to run the app
CMD ["streamlit", "run", "app.py", "--server.port", "7860", "--server.address", "0.0.0.0", "--server.enableCORS", "false", "--server.enableXsrfProtection", "false"]
