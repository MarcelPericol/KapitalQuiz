import threading
import time
import sys

def timed_input(prompt, timeout):
    user_input = [None]
    stop_flag = [False]

    def read_input():
        user_input[0] = input(prompt)
        stop_flag[0] = True

    thread = threading.Thread(target=read_input)
    thread.daemon = True
    thread.start()

    start = time.time()
    last_remaining = None

    while time.time() - start < timeout:
        if stop_flag[0]:
            return user_input[0], False

        remaining = int(timeout - (time.time() - start))

        # Only print when the number changes
        if remaining != last_remaining:
            sys.stdout.write(f"\nTime left: {remaining:2d} seconds\n")
            sys.stdout.flush()
            last_remaining = remaining

        time.sleep(1)

    stop_flag[0] = True
    return None, True
