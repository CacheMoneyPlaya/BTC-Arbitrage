from crontab import CronTab


cron = CronTab(user='root')
job = cron.new(command='python3 ~root/arbitrage_opp/test2.py')
job.minute.every(1)
cron.write
