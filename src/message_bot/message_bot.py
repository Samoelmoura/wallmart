import requests
from airflow import DAG
from airflow.operators.python import PythonOperator
import datetime

token = '6621564816:AAHszMr8czAq29KJDEPeVbOZpIZ2U74U5p0'
chat_id = '586530904'

default_args={
    'owner':'samoel',
    'depends_on_past':False,
    'retries':5,
    'retry_delay':datetime.timedelta(minutes=5)
}

dag = DAG(
    default_args=default_args,
    dag_id='send_message_dag',
    schedule_interval=datetime.timedelta(minutes=1),
    init_date = datetime.datetime(2023, 9, 21)
)

task1 = PythonOperator(
    dag=dag,
    python_callable=send_message('Olá Samoel, está um lindo dia hoje!'),
    provide_context=True,
    task_id='send_message_task'
)

def send_message(text):
    url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}'
    r = requests.post(url=url, json={'text':text})
    print(r.status_code)