
from airflow.utils.email import send_email

def notify_email(context):
    subject = f"Airflow Task Failed: {context['task_instance'].task_id}"
    html_content = f"""
    <p>DAG: {context['dag'].dag_id}</p>
    <p>Task: {context['task_instance'].task_id}</p>
    <p>Execution Time: {context['execution_date']}</p>
    <p>Log URL: <a href="{context['task_instance'].log_url}">{context['task_instance'].log_url}</a></p>
    """
    send_email(to=["admin@example.com"], subject=subject, html_content=html_content)
