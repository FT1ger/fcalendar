import datetime
import email
from icalendar import Calendar, Event,Timezone
from email.parser import BytesParser
from email import policy
import pandas as pd
filepath = 'Your Potential Timetable.eml'
import re
import uuid

with open(filepath) as email_file:
    email_message = email.message_from_file(email_file)
content = (email_message.get_payload())

content1 = content.replace('=\n','')
new_p = re.compile('<td.*?>.*?</td>')
lst1 = new_p.findall(content1)
lst1 = lst1[:-1]

clear_p = re.compile('</*?td.*?>')
for i in range(len(lst1)):
    lst1[i] = re.sub(clear_p,'',lst1[i])

# reshape the list to a 2d array
lst2 = []
for i in range(len(lst1)//9):
    lst2.append([])
    for j in range(9):
        lst2[i].append(lst1[9*i+j])

# sort all the codes in pandas dataframe
df = pd.DataFrame(lst2)
df.columns = ['status','class','section','subject','course','seats open','duration&locations','dates','campus']
time_loc = df["duration&locations"]
for i in range(len(time_loc)):
    time_loc[i] = time_loc[i].split('<br />')

dura = df['dates']
for i in range(len(dura)):
    dura[i] = dura[i].split('<br />')
# start time & end time -> datetime.datetime
def duration(duradate:str):
    duradate = duradate.split(' - ')
    start = datetime.datetime.strptime(duradate[0], '%d/%m/%Y')
    end = datetime.datetime.strptime(duradate[1], '%d/%m/%Y')
    return(start,end)

dura_date = []
for i in range(len(dura)):
    for j in range(len(dura[i])):
        dura[i][j] = duration(dura[i][j])
# dura[i][j][0] = starttime,dura[i][j][1] = endtime
# i = course,j = time duration

# seperate time & location
p2 = r"^([MTWFS][a-z]*)\s([\d:amp\s]+)-([\d:amp\s]+)-\s(.+)$"
match = re.match(p2,time_loc[0][0])

weeks = []
time_start = []
time_end = []
location = []
for i in range(len(time_loc)):
    weeks.append([])
    time_start.append([])
    time_end.append([])
    location.append([])
    for j in range(len(time_loc[i])):
        match = re.match(p2,time_loc[i][j])
        weeks[i].append(match.group(1))
        time_start[i].append(match.group(2).strip())
        time_end[i].append(match.group(3).strip())
        location[i].append(match.group(4))

# create event
def create_event(cal,course:str,start_date,end_date,start_time,end_time,location,campus):
    day = start_date
    while day <= end_date:
        event = Event()
        event.add("DTSTART", datetime.datetime.strptime((str(day.date())+' '+start_time),'%Y-%m-%d %I:%M%p'))
        event.add("DTEND", datetime.datetime.strptime((str(day.date())+' '+end_time),'%Y-%m-%d %I:%M%p'))
        event.add("CREATED", datetime.datetime.now())
        event.add("UID", uuid.uuid4())
        event.add("SUMMARY", course)
        event.add("DESCRIPTION", campus)
        event.add("LOCATION", location)
        day += datetime.timedelta(days = 7)
        cal.add_component(event)

with open('Your_timetable.ics','wb') as f:
    cal = Calendar()
    for i in range(len(df['subject'])):
        for j in range(len(dura[i])):
            create_event(cal,df['subject'][i]+' '+df['course'][i],dura[i][j][0],dura[i][j][1],time_start[i][j],time_end[i][j],location[i][j],df['campus'][i])
    f.write(cal.to_ical())