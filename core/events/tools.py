from datetime import datetime, timedelta
import json
ip_time_post = {}


def access_ip(ip):
    try:
        time_last = ip_time_post[ip]
    except KeyError:
        ip_time_post[ip] = datetime.now()
        return (True, 0)
    time_now = datetime.now()
    time = (time_now - time_last).total_seconds()
    if time > 60:
        ip_time_post[ip] = time_now
        return (True, 0)
    return (False, time)


def form_message(time):
    sec = str(time).split('.')[0]
    data = {'error': 'service timeout',
            'time': 60 - int(sec)}
    d = json.dumps(data, ensure_ascii=False)
    print(d)
    return d
