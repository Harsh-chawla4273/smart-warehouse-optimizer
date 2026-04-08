FROM python:3.9
WORKDIR /code
RUN pip install --no-cache-dir flask streamlit pandas plotly numpy
COPY . .
EXPOSE 7860
# Dashboard background mein chalega, API front mein
CMD python inference.py & streamlit run app.py --server.port 8501 --server.address 0.0.0.0
