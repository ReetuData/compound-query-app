FROM python:3.10

WORKDIR /app

EXPOSE 8500

COPY . /app/

RUN pip install -r /app/requirements.txt

CMD streamlit run /app/pandasai_demo.py --server.port 8500