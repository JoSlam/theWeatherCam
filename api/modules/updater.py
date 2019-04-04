from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from modules import weather_updater

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(weather_updater.update_forecast, 'interval', minutes=5)
    scheduler.start()