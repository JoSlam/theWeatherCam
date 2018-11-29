from subprocess import Popen
import shlex
import time

if __name__ == "__main__":
    while True:
        args = shlex.split('python manage.py upload_data')
        proc = Popen(args)
        time.sleep(7200)