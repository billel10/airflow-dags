from airflow.sdk import dag, task
from datetime import datetime

@dag(
    dag_id="simple_dag",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
)
def simple_dag():

    @task
    def hello():
        print("Hello Airflow")

    hello()

simple_dag()
