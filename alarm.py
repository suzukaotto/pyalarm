import time
from datetime import datetime, timedelta
import pygame

target_time = "1253"
notice_time = ["0100", "0030", "0020", "0010", "0005", "0002", "0001"]
mp3_file = "God-Chang-seop-_신창섭_-_바로-리부트-정상화_-MV.mp3"
triggered_alarms = set()

def play_mp3(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)
    pygame.mixer.quit()

def time_difference(now, target_time):
    now_time = datetime.strptime(now, "%H%M")
    target_time = datetime.strptime(target_time, "%H%M")
    
    if now_time > target_time:
        target_time += timedelta(days=1)
    
    difference = target_time - now_time
    difference_in_minutes = difference.total_seconds() // 60
    hours, minutes = divmod(difference_in_minutes, 60)
    
    return f"{int(hours):02d}{int(minutes):02d}"

def check_time_and_play(target_time, file_path):
    print(f"Setted alarm: {target_time[:2]}:{target_time[2:]}")
    while True:
        now = datetime.now().strftime("%H%M")
        time_diff = time_difference(now, target_time)
        
        if time_diff in notice_time and time_diff not in triggered_alarms:
            print(f"Remain {time_diff[:2]} hours {time_diff[2:]} minutes")
            triggered_alarms.add(time_diff)
        
        if now == target_time and now not in triggered_alarms:
            print(f"Alarm!")
            play_mp3(file_path)
            triggered_alarms.add(now)
            break
        time.sleep(1)

check_time_and_play(target_time, mp3_file)