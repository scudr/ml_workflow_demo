from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from get_data_kaggle import get_data_kaggle
from automl import MLSystem

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 3, 26),
    'email': ['enriquejmiagamarra@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'ml_workflow_demo',
    default_args=default_args,
    description='A simple ML pipeline',
    schedule_interval='0 17 * * *',
)

def load_data():
    ml_system = MLSystem('data/train.csv', 'Target')
    ml_system.load_data()

def train_model():
    ml_system = MLSystem('data/train.csv', 'Target')
    ml_system.train_model()

def tune_model():
    ml_system = MLSystem('data/train.csv', 'Target')
    ml_system.tune_model()

get_data_kaggle_task = PythonOperator(
    task_id='get_data_kaggle',
    python_callable=get_data_kaggle,
    dag=dag,
)

load_data_task = PythonOperator(
    task_id='load_data',
    python_callable=load_data,
    dag=dag,
)

train_model_task = PythonOperator(
    task_id='train_model',
    python_callable=train_model,
    dag=dag,
)

tune_model_task = PythonOperator(
    task_id='tune_model',
    python_callable=tune_model,
    dag=dag,
)

get_data_kaggle_task >> load_data_task >> train_model_task >> tune_model_task
