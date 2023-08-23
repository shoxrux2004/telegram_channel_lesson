from read_data import fromJson
import datetime

def get_posts_peer_day(data:dict, day:str)->int:
    """
    Return the number of posts for given day

    Args:
        data (dict): a dictionary of posts

    Returns: 
        dict: a dictionary with the number of posts for each month
    """
    msgs=data.get('messages')
    ansver={}
    for mgs in msgs:
        date=mgs['date']
        date=datetime.datetime.strptime(date,'%Y-%m-%dT%H:%M:%S')
        y=date.year
        d=date.day
        month=date.month
        ansver.setdefault(month,{})
        month_day:dict=ansver[month]
        month_day['day']=day
        count=month_day.setdefault('count',0)
        if day==d:
            month_day['day']+=1 
    return ansver
data=fromJson('data/result.json')
print(get_posts_peer_day(data,3))