import datetime
import email
from email.parser import BytesParser
from email import policy
filepath = 'Your Potential Timetable_2.eml'
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
for i in range(9):
    lst2.append([])
    for j in range(len(lst1)//9):
        lst2[i].append(lst1[9*j+i])

# sort all the codes in list
# lst = ['status','class','section','subject','course','seats open','duration&locations','dates','campus']
# sometime one course only have one duration, to fix this, add another layer of structure
# sometime eml has different form, try to fix it
# still need more form from different email
time_loc = lst2[6]
for i in range(len(time_loc)):
    if "<br />" in time_loc[i]:
        time_loc[i] = time_loc[i].split('<br />')
    elif "<br>" in time_loc[i]:
        time_loc[i] = time_loc[i].split('<br>')
    elif "<br/>" in time_loc[i]:
        time_loc[i] = time_loc[i].split('<br/>')
    else:
        time_loc[i] = [time_loc[i]]
    
dura = lst2[7]
for i in range(len(dura)):
    if "<br />" in dura[i]:
        dura[i] = dura[i].split('<br />')
    elif "<br>" in dura[i]:
        dura[i] = dura[i].split('<br>')
    elif "<br/>" in dura[i]:
        dura[i] = dura[i].split('<br/>')
    else:
        dura[i] = [dura[i]]

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

# create event for one course
def create_event(course:str,start_date,end_date,start_time,end_time,location,campus):
    day = start_date
    course_events = ''
    while day <= end_date:
        event = "\nBEGIN:VEVENT"
        event += f"\nSUMMARY:{course}"
        start = datetime.datetime.strptime((str(day.date())+' '+start_time),'%Y-%m-%d %I:%M%p')
        event += f"\nDTSTART:{start.strftime('%Y%m%dT%H%M%S')}"
        end = datetime.datetime.strptime((str(day.date())+' '+end_time),'%Y-%m-%d %I:%M%p')
        event += f"\nDTEND:{end.strftime('%Y%m%dT%H%M%S')}"
        event += f"\nUID:{uuid.uuid4()}"
        event += f"\nCREATED:{datetime.datetime.now().strftime('%Y%m%dT%H%M%S')}"
        event += f"\nDESCRIPTION:{campus}"
        event += f"\nLOCATION:{location}"
        day += datetime.timedelta(days = 7)
        event += "\nEND:VEVENT"
        course_events += event
    return course_events

with open('Your_timetable.ics','w') as f:
    cal = 'BEGIN:VCALENDAR'
    for i in range(len(lst2[3])):
        for j in range(len(dura[i])):
            cal += create_event(lst2[3][i]+' '+ lst2[4][i],dura[i][j][0],dura[i][j][1],time_start[i][j],time_end[i][j],location[i][j],lst2[8][i])
    cal += '\nEND:VCALENDAR'
    f.write(cal)