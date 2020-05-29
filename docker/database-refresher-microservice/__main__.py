from apscheduler.schedulers.blocking import BlockingScheduler

from main import refresh_database

def start_scheduler():
    """ run refresh_database every morning at 03 am  """
    scheduler = BlockingScheduler()
    scheduler.add_job(
        refresh_database,
        max_instances=1,
        replace_existing=False,
        trigger="cron",
        minute="00",
        hour="03",
    )
    scheduler.start()


refresh_database()
start_scheduler()
