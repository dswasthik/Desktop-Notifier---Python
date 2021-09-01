from plyer import notification  
import time

def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "D:\\Resume projects\\Notifier\\clock-icon.png",
        timeout = 10,
    )


if __name__ == '__main__':
    while True:
        notifyMe("Hey Swasthik , take a break now !!")
        time.sleep(1200)