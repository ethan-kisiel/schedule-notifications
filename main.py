from schedule import Schedule
import time, os, environ_vars
os.environ['SENDER_EMAIL'] = 'notifications.sms.sender@gmail.com'
os.environ['PASSWORD'] = 'm4t7zmaWhQAFs4j'
os.environ['SMTP_SERVER'] = 'smtp.gmail.com'
os.environ['RECIPIENT_EMAIL'] = '8146556090@vtext.com'

if __name__ == '__main__':
    limits = [4,2, 3, 9, 5, 52]
    new_schedule = Schedule('Schedule.xlsx', limits)
    
    SENDER_EMAIL = os.environ.get('SENDER_EMAIL')
    PASSWORD = os.environ.get('PASSWORD')
    RECIPIENT_EMAIL = os.environ.get('RECIPIENT_EMAIL')
    SMTP_SERVER = os.environ.get('SMTP_SERVER')
    
    while True:
        for slot in new_schedule.get_day():
            if new_schedule.compare_time(slot, 5):
                s = new_schedule.start_mail_server(SMTP_SERVER, [SENDER_EMAIL, PASSWORD])
                new_schedule.send_notification(s, RECIPIENT_EMAIL, slot, new_schedule.get_day()[slot])
                time.sleep(600)