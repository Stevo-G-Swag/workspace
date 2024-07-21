import logging

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from flask import current_app

scheduler = BackgroundScheduler()

def schedule_task(task_func, run_date=None, cron_string=None):
    try:
        if run_date:
            job = scheduler.add_job(task_func, 'date', run_date=run_date)
            current_app.logger.info('Task scheduled for %s', run_date)
        elif cron_string:
            job = scheduler.add_job(task_func, CronTrigger.from_crontab(cron_string))
            current_app.logger.info('Task scheduled with cron string: %s', cron_string)
        else:
            raise ValueError('No valid date or cron string provided for task scheduling')
        return job.id
    except Exception as e:
        current_app.logger.error('Error scheduling task: %s', str(e), exc_info=True)
        raise

def modify_task(job_id, run_date=None, cron_string=None):
    try:
        job = scheduler.get_job(job_id)
        if job:
            if run_date:
                job.modify(next_run_time=run_date)
                current_app.logger.info('Task %s modified to run at %s', job_id, run_date)
            elif cron_string:
                job.reschedule(trigger=CronTrigger.from_crontab(cron_string))
                current_app.logger.info('Task %s rescheduled with new cron string: %s', job_id, cron_string)
            else:
                raise ValueError('No valid date or cron string provided for task modification')
        else:
            raise ValueError(f'No task found with job ID: {job_id}')
    except Exception as e:
        current_app.logger.error('Error modifying task: %s', str(e), exc_info=True)
        raise

def remove_task(job_id):
    try:
        scheduler.remove_job(job_id)
        current_app.logger.info('Task %s removed successfully', job_id)
    except Exception as e:
        current_app.logger.error('Failed to remove task with job ID: %s. Error: %s', job_id, str(e), exc_info=True)
        raise

def start_scheduler():
    try:
        scheduler.start()
        current_app.logger.info('Scheduler started')
    except Exception as e:
        current_app.logger.error('Failed to start scheduler. Error: %s', str(e), exc_info=True)
        raise