import schedule,time
def job():
    print('I\'m working...')
schedule.every(2).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
