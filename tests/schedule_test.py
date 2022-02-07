import os, schedule, environ_vars

from datetime import time
SCHEDULE = os.environ.get('SCHEDULE')
test_schedule = schedule.Schedule(SCHEDULE, [4,2, 3, 10, 5, 52])

def test_convert_time():
    assert test_schedule.convert_time(time(12,00)) == '12:00:PM'
    assert test_schedule.convert_time(time(11,55)) == '11:55:AM'
    assert test_schedule.convert_time(time(23,00)) == '11:00:PM'
    assert test_schedule.convert_time(time(0,00)) == '12:00:AM'
    
def test_compare_time():
    target_time = test_schedule.convert_time(time(7,00))
    current_time = test_schedule.convert_time(time(12,55))
    assert test_schedule.compare_time(target_time, 5, current_time) == False
    
    target_time = test_schedule.convert_time(time(7,0))
    current_time = test_schedule.convert_time(time(6,55))
    assert test_schedule.compare_time(target_time, 5, current_time) == True
    
    target_time = test_schedule.convert_time(time(12,00))
    current_time = test_schedule.convert_time(time(11,55))
    assert test_schedule.compare_time(target_time, 5, current_time) == True
    
    
    