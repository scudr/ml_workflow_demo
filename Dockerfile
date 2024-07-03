# FROM apache/airflow:2.9.2

# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# USER airflow

# COPY dags/ /opt/airflow/dags/




# FROM apache/airflow:2.9.2

# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# USER airflow

# COPY dags/ /opt/airflow/dags/
# COPY dags/kaggle.json /home/airflow/.kaggle/kaggle.json
# RUN chmod 600 /home/airflow/.kaggle/kaggle.json






FROM apache/airflow:2.8.0
# FROM apache/airflow:2.9.2-python3.9
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Cambiar a usuario root para crear el directorio y copiar el archivo
USER root

RUN mkdir -p /home/airflow/.kaggle && \
    chown -R airflow: /home/airflow/.kaggle

COPY dags/kaggle.json /home/airflow/.kaggle/kaggle.json

# Cambiar permisos del archivo kaggle.json
RUN chmod 600 /home/airflow/.kaggle/kaggle.json && \
    chown airflow: /home/airflow/.kaggle/kaggle.json

# Volver a usuario airflow
USER airflow

COPY dags/ /opt/airflow/dags/


# FROM apache/airflow:2.9.2

# USER airflow

# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# COPY dags/ /opt/airflow/dags/



# FROM apache/airflow:2.9.2

# USER airflow

# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# USER airflow

# COPY dags/  /opt/airflow/dags/
