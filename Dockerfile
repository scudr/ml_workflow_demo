FROM apache/airflow:2.8.3

COPY requirements.txt /requirements.txt


# Set environment variable to bypass sklearn deprecation issue
ENV SKLEARN_ALLOW_DEPRECATED_SKLEARN_PACKAGE_INSTALL=True

RUN pip install --user --upgrade pip
RUN pip install --no-cache-dir --user -r /requirements.txt

# Optionally, explicitly upgrade PyCaret or install with extras
RUN pip install --upgrade pycaret

# Copy the dags directory
COPY dags/ /opt/airflow/dags/

# Ensure the .kaggle directory exists and copy the kaggle.json file
RUN mkdir -p /home/airflow/.kaggle
COPY dags/kaggle.json /home/airflow/.kaggle/kaggle.json


# Set correct permissions
USER root
RUN chmod -R 755 /home/airflow/.kaggle

# RUN chown -R airflow: /home/airflow/.kaggle

USER airflow



# FROM apache/airflow:2.8.3

# COPY requirements.txt /requirements.txt

# RUN pip install --user --upgrade pip
# RUN pip install --no-cache-dir --user -r /requirements.txt

# # Copy the dags directory
# COPY dags/ /opt/airflow/dags/














# USER root

# RUN mkdir -p /home/airflow/.kaggle && \
#     chown -R airflow: /home/airflow/.kaggle

# COPY dags/kaggle.json /home/airflow/.kaggle/kaggle.json

# # Cambiar permisos del archivo kaggle.json
# RUN chmod 600 /home/airflow/.kaggle/kaggle.json && \
#     chown airflow: /home/airflow/.kaggle/kaggle.json

# # Volver a usuario airflow
# USER airflow

# COPY dags/ /opt/airflow/dags/
