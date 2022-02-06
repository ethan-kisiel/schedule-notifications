from schedule import Schedule
import time, os, environ_vars
from datetime import datetime
os.environ['SENDER_EMAIL'] = 'notifications.sms.sender@gmail.com'
os.environ['PASSWORD'] = 'm4t7zmaWhQAFs4j'
os.environ['SMTP_SERVER'] = 'smtp.gmail.com'
os.environ['RECIPIENT_EMAIL'] = '8146556090@vtext.com'

if __name__ == '__main__':
    limits = [4,2, 3, 10, 5, 52]
    new_schedule = Schedule('Schedule.xlsx', limits)

    TWILIO_SID = os.environ.get('TWILIO_SID')
    TWILIO_AUTH = os.environ.get('TWILIO_AUTH')
    TWILIO_NUMBER = os.environ.get('TWILIO_NUMBER')
    
    RECIPIENT_NUMBER = os.environ.get('RECIPIENT_NUMBER')
    
    while True:
        for slot in new_schedule.get_day():
            if new_schedule.compare_time(slot, 5):
                msg = f'({slot}) {new_schedule.get_day()[slot]}'
                new_schedule.send_notification(TWILIO_SID, TWILIO_AUTH, RECIPIENT_NUMBER, TWILIO_NUMBER, msg)
                
                current_time = new_schedule.convert_time(datetime.now().strftime('%H:%M'))
                print(f'Sent Message at {current_time}')
                time.sleep(600)