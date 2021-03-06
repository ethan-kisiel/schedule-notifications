import openpyxl
from datetime import datetime
from twilio.rest import Client

class Schedule:
    '''
    '''
    def __init__(self, schedule: str, limits):
        self.schedule = schedule
        self.schedule_data = self.get_data(*limits)
        self.days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        
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
        if int(time[0]) == 0:
            time[0] = '12'
            return(f'{time[0]}:{time[1]}:AM')
        elif int(time[0]) == 12:
            return(f'{time[0]}:{time[1]}:PM')
        elif int(time[0]) > 12:
            time[0] = str(int(time[0]) - 12)
            return(f'{time[0]}:{time[1]}:PM')
        else:
            return(f'{int(time[0])}:{time[1]}:AM')

    def compare_time(self, time: str, buffer: int, curr_time: str=None):
        '''
        Takes time in the format of HH:MM:AM/PM
        returns true if time is within buffer(minutes) of current time
        '''

        current_time = datetime.now()
        current_time = self.convert_time(current_time.strftime('%H:%M')).split(':')
        if curr_time is not None:
            current_time = curr_time.split(':')
        time = time.split(':')

        target_hour = int(time[0])
        target_minute = int(time[1])
        target_cycle = time[2]
        current_hour = int(current_time[0])
        current_minute = int(current_time[1])
        current_cycle = current_time[2]
        
        if current_cycle == target_cycle and current_hour - target_hour == 11:
            target_hour = 13 # hack for transition from 12 -> 1 edgecase
        if target_hour == 12:
            if current_cycle == target_cycle and current_hour == target_hour:
                if target_minute - current_minute <= buffer and target_minute > current_minute:
                    return True
                else:
                    return False
            else:
                if current_cycle == target_cycle:
                    return False
                elif target_hour - current_hour == 1 and current_minute >= target_minute + (60-buffer):
                    return True
                else:
                    return False
        elif current_cycle != target_cycle:
            return False
        elif target_hour - current_hour == 1 and current_minute >= target_minute + (60 - buffer):
            return True
        elif current_hour == target_hour and target_minute - current_minute <= buffer:
            if current_minute > target_minute:
                return False
            else:
                return True
        else:
            return False

    def get_day(self):
        today = datetime.today().weekday()
        try:
            return self.schedule_data[self.days[today]]
        except KeyError:
            print(self.schedule_data)

    def send_notification(self, twilio_sid, twilio_auth, to_number, from_number, msg):
        '''
        Takes twilio account sid, twilio authentication token, target number, twilio number, message body
        '''
        try:
            client = Client(twilio_sid, twilio_auth)
            message = client.messages.create(
                to=to_number,
                from_=from_number,
                body=msg
            )
        except Exception as e:
            print(e)
