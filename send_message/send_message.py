import requests
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import timedelta
from datetime import datetime
import openai

token = 'xxx'
openai.api_key = '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'
chat_id = '586530904'
url = f'https://api.telegram.org/bot6464394089:AAFfCKVcvoEuMYLZuIDeNKpRP_mdiEg0XB8/sendMessage?chat_id={chat_id}'

def send_message():
    question = f'Olá, me conte uma breve história sobre um país aleatório em 3 linhas'
    completion = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[{'role':'user',
                'content':question}]
    )
    text = completion.choices[0].message.content
    r = requests.post(url=url, json={'text':text})
    return None


default_args = {
    'owner':'samoel',
    'depends_on_past':False,
    'retries':5,
    'retry_delay':timedelta(minutes=5)
}


dag = DAG(
    default_args=default_args,
    dag_id='send_message_dag',
    start_date=datetime(2023, 10, 5),
    schedule_interval=timedelta(minutes=1)
)


task1 = PythonOperator(
    dag=dag,
    provide_context=True,
    python_callable=send_message,
    task_id='send_message_task'
)
