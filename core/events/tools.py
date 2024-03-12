from datetime import datetime


ip_time_post = {}


def access_ip(ip: str) -> bool:
    try:
        time_last = ip_time_post[ip]
    except KeyError:
        ip_time_post[ip] = datetime.now()
        return True
    time_now = datetime.now()
    time = (time_now - time_last).total_seconds()
    if time > 60:
        ip_time_post[ip] = time_now
        return True
    return False
