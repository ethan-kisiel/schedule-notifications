import openpyxl, smtplib, ssl
from datetime import datetime

class Schedule:
    '''
    '''
    def __init__(self, schedule):
        self.schedule = schedule
        self.schedule_data = self.get_data()
        
    def get_data(self):
        '''
        Returns a dictionary based on spreadsheet data
        '''
        
    def start_mail_server(self, smtp_server: str, mailer_email: str):
        self.mailer_email = mailer_email
        
    def convert_time(self, time):
        '''
        Takes 24 hour time and converts to 12 hour time
        '''

    def compare_time(self, time: str, buffer: int):
        '''
        Takes time in the format of HH:MM AM/PM
        returns true if time is within buffer(minutes) of current time
        '''
    
    def send_notification(self, recipient: str, subject: str, body: str):
        '''
        '''
