import os
import pandas as pd
from airflow import DAG
from datetime import timedelta, datetime
from airflow.operators.python import PythonOperator, ShortCircuitOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook

workdir = '/home/samoel/pessoal/projetos/wallmart/catch_data/csv'
files = os.listdir(workdir)

csv_files = [file for file in files if file.endswith('.csv')]

def search_csv_files(**context):
    if csv_files:
        for csv_file in csv_files:
            complete_file_name = workdir + '/' + csv_file
            df = pd.read_csv(complete_file_name)
            context['ti'].xcom_push(key='df', value=df)
            context['ti'].xcom_push(key='complete_file_name', value=complete_file_name)
        return True
    else:
        return False


def insert_into(**context):
    df = context['ti'].xcom_pull(key='df', task_ids='task1')
    complete_file_name = context['ti'].xcom_pull(key='complete_file_name', task_ids='task1')
    hook = PostgresHook(postgres_conn_id='conn_postgres')
    for ix, row in df.iterrows():
        hook.run(f"""
        CREATE TABLE IF NOT EXISTS test(
            Store INT,
            Dept INT,
            Date VARCHAR,
            Weekly_Sales FLOAT,
            IsHoliday VARCHAR
        );
        INSERT INTO test(
            Store,
            Dept,
            Date
            Weekly_Sales,
            IsHoliday
        )
        VALUES(
            {row['Store']},
            {row['Dept']},
            {row['Date']},
            {row['Weekly_Sales']},
            {row['IsHoliday']},
        );
        """)
    os.remove(complete_file_name)
    return None


default_args = {
    'owner':'samoel',
    'depends_on_past':False,
    'retries':5,
    'retry_delay':timedelta(minutes=5)
}


dag = DAG(
    default_args=default_args,
    dag_id='catch_sales',
    start_date=datetime(2023, 10, 10),
    schedule_interval=timedelta(hours=1)
)


task1 = PythonOperator(
    dag=dag,
    task_id='task1',
    provide_context=True,
    python_callable=search_csv_files
)


task2 = PythonOperator(
    dag=dag,
    task_id='task2',
    provide_context=True,
    python_callable=insert_into
)


task3 = ShortCircuitOperator(
    dag=dag,
    task_id='task3',
    provide_context=True,
    python_callable=search_csv_files
)


task4 = DummyOperator(
    task_id='task4',
    dag=dag
)


task1 >> task2 >> task3
task2 >> task4