import os, schedule, environ_vars

from datetime import time
SCHEDULE = os.environ.get('SCHEDULE')
test_schedule = schedule.Schedule(SCHEDULE, [4,2, 3, 10, 5, 52])

def test_convert_time():
    assert test_schedule.convert_time(time(12,00)) == '12:00:PM'
    assert test_schedule.convert_time(time(11,55)) == '11:55:AM'
    assert test_schedule.convert_time(time(23,00)) == '11:00:PM'
    assert test_schedule.convert_time(time(0,00)) == '12:00:AM'
    assert test_schedule.convert_time(time(23,55)) == '11:55:PM'
    
def test_compare_time():
    
    # 11:55 pm current time  12:00 am target time == true
    target_time = test_schedule.convert_time(time(0,0))
    current_time = test_schedule.convert_time(time(23,55))
    assert test_schedule.compare_time(target_time, 5, current_time) == True
    
    # 7 am target time and 6:55 am current time == true
    target_time = test_schedule.convert_time(time(7,0))
    current_time = test_schedule.convert_time(time(6,55))
    assert test_schedule.compare_time(target_time, 5, current_time) == True
    
    # 12:00 pm target time and 11:55 am current time == true
    target_time = test_schedule.convert_time(time(12,00))
    current_time = test_schedule.convert_time(time(11,55))
    assert test_schedule.compare_time(target_time, 5, current_time) == True
    
    # 12:55  am current time and 1 am target time == true
    target_time = test_schedule.convert_time(time(1,00))
    current_time = test_schedule.convert_time(time(0,55))
    assert test_schedule.compare_time(target_time, 5, current_time) == True
    
    # 3:55 am target time and 4:00 pm current time == false
    target_time = test_schedule.convert_time(time(3,55))
    current_time = test_schedule.convert_time(time(16,00))
    assert test_schedule.compare_time(target_time, 5, current_time) == False
    
    # 1 am target time and 12:55 pm current time == false
    target_time = test_schedule.convert_time(time(1,00))
    current_time = test_schedule.convert_time(time(12,55))
    assert test_schedule.compare_time(target_time, 5, current_time) == False
    
    # 12 pm target time and 11:55 pm current time == false
    target_time = test_schedule.convert_time(time(12,0))
    current_time = test_schedule.convert_time(time(23,55))
    assert test_schedule.compare_time(target_time, 5, current_time) == False
    
    # 7 am target time and 12:55 pm current time == false
    target_time = test_schedule.convert_time(time(7,00))
    current_time = test_schedule.convert_time(time(12,55))
    assert test_schedule.compare_time(target_time, 5, current_time) == False
    
