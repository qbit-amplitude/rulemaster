import datetime
from rulemaster.celery import app

@app.task
def health_check():
    now = datetime.datetime.now().isoformat()
    print(now)