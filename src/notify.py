from notify_run import Notify

notify = Notify()
info = str(notify.register())

f = open('config.txt', 'w')
f.write(info)
f.close()

_ = input()