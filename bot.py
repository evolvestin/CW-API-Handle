import os
import objects
from api import ChatWars
stamp1 = objects.time_now()
cw = ChatWars(os.environ['LOGIN'], os.environ['PASS'])
objects.start_message(None, stamp1)


def api_handler():
    global cw
    while True:
        try:
            cw.run()  # this blocks execution
        except KeyboardInterrupt:
            cw.stop()


if __name__ == '__main__':
    api_handler()
