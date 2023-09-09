%%writefile run_dummy.py

import time
from datetime import datetime


def run_dummy(life_time=1*60, printing_duration=10):
    # time unit: minutes
    print_dur_seconds=printing_duration * 60

    # keep_serving=True

    # Get the current date and time
    # current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    start = datetime.now()

    # while keep_serving:
    for i in range(int(life_time/printing_duration)+1):
        time.sleep(print_dur_seconds)
        dur = datetime.now() - start
        print("Dummy has been running for:", dur)
        
        
if __name__=='__main__':
    run_dummy(0.3,0.1)
