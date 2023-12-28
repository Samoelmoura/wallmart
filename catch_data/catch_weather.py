import requests
import pandas as pd
from datetime import timedelta, datetime
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook

from airflow import DAG

def api_request(**context):
    url = "https://weatherapi-com.p.rapidapi.com/current.json"
    querystring = {"q":"Ribeirao Preto"}
    headers = {
        "X-RapidAPI-Key": "1d12d350f3msha27237947fa943ap1b053ejsne8059d7bfe42",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    if response:
        data = response.json()
        context['ti'].xcom_push(key='data', value='data')
    else:
        print(f'A requisição falhou, status {response.status_code}')
    return None


def insert_into_database(**context):
    data = context['ti'].xcom_pull(key='data', task_ids='task1')
    df = pd.DataFrame(index=[0])
    df['datetime'] = data['location']['localtime']
    df['temperature'] = df['current']['temp_c']
    hook = PostgresHook(conn_postgres='conn_postgres')
    for ix, row in df.iterrows():
        hook.run(f"""
            CREATE TABLE IF NO EXISTS usa_weather(
                datetime VARCHAR(50),
                temperature INT(8)
            );

            INSERT INTO usa_weather()
                datetime,
                temperature
            )
            VALUES(
                '{df['datetime']}',
                {df['temperature']}
            );
        """)


default_args = {
    'owner':'samoel',
    'depends_on_past':False,
    'retries':5,
    'retry_delay':timedelta(minutes=5)
}

dag = DAG(
    dag_ig='catch_weather',
    default_args=default_args,
    start_date=datetime(2023, 12, 10),
    schedule_interval=timedelta(days=1),
)

task1 = PythonOperator(
    taskid='task1',
    dag=dag,
    provide_context=True,
    python_callable=api_request
)

task2 = PythonOperator(
    taskid='task1',
    dag=dag,
    provide_context=True,
    python_callable=insert_into_database,
)