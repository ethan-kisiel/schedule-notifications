from numpy import array
import openpyxl, smtplib, ssl
from datetime import datetime

class Schedule:
    '''
    '''
    def __init__(self, schedule: str, limits: array):
        self.schedule = schedule
        self.schedule_data = self.get_data(*limits)
        
    def get_data(self, title_row: int, title_col, min_col: int, max_col: int, min_row: int, max_row: int):
        '''
        '''
        try:
            wb = openpyxl.load_workbook(self.schedule, data_only=True)
            ws = wb.active
            sched_dict = {}
            # set up dictionary with day values
            for col in range(min_col, max_col):
                curr_row_title = ws.cell(row=title_row, column=col).value
                if curr_row_title != None:
                    sched_dict[curr_row_title] = dict()
                for row in range(min_row, max_row):
                    curr_cell = ws.cell(row=row, column=col).value
                    curr_col_title = ws.cell(row=row, column=title_col).value
                    if curr_cell != None:
                        sched_dict[curr_row_title][self.convert_time(curr_col_title)] = curr_cell
            return sched_dict
        except FileNotFoundError:
            print('ERROR: file not found.')

    def convert_time(self, time: datetime.time):
        '''
        Takes datetime.time
        returns string in 12 hour format
        '''
        time = str(time).split(':')
        if len(time) > 2:
            time.pop(2)
        if int(time[0]) > 12:
            time[0] = str(int(time[0]) - 12)
            return(f'{time[0]}:{time[1]}:PM')
        else:
            return(f'{time[0]}:{time[1]}:AM')
    
    def compare_time(self, time: str, buffer: int):
        '''
        Takes time in the format of HH:MM:AM/PM
        returns true if time is within buffer(minutes) of current time
        '''

    def start_mail_server(self, smtp_server: str, mailer: array, context=None, port: int=None):
        '''
        Starts SMTP server instance via given smtp_server, mailer[email, password], and context
        '''
        self.mailer_email = mailer[0]
        mailer_password = mailer[1]
        
        if context is None:
            context = ssl.create_default_context()
        if port is None:
            port = 587
            
        try:
            self.server = smtplib.SMTP(smtp_server, port)
            self.server.ehlo()
            self.server.starttls(context=context)
            self.server.ehlo()
            self.server.login(self.mailer_email, mailer_password)

        except Exception as e:
            print(e)

    def end_mail_server(self):
        self.server.quit()
    
    def send_notification(self, recipient: str, subject: str, body: str):
        '''
        '''
        try:
            self.server.send_message()
        except Exception as e:
            print(e)
