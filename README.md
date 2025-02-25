# FCalendar
FCalendar is a small tool for student in the University of Adelaide which can read your schedule from email and generate an iCalandar (.ics) file, which can be imported to your Calendar app.

## How can I use FCalendar

1. Open your Timetable Planner.(https://access.adelaide.edu.au/sa/student/TimeTablePlanner.asp)
![](https://github.com/FT1ger/fcalendar/blob/main/images/timetableplanner.png)
2. Generate your Timetable.
![](https://github.com/FT1ger/fcalendar/blob/main/images/generate.png)
3. Click "View".
![](https://github.com/FT1ger/fcalendar/blob/main/images/view.png)
4. Click the "Email" button (at the left-top of this page).
![](https://github.com/FT1ger/fcalendar/blob/main/images/mail.png)
5. Send it to your email.
6. Download the email file and place it in the same directory of `FCalendar.py`.(Its name should be "`Your Potential Timetable.eml`")
![](https://github.com/FT1ger/fcalendar/blob/main/images/download.png)
7. Run FCalendar.py (or FCalendar.ipynb in your jupyter notebook)
8. Generate a file "`Your_timetable.ics`", send it to your phone or import it to your calendar app.

(If you are using iOS, strongly advise you create a new calendar to manage all the events.)
(Suggest to use school email(outlook) or gmail, if you find some bug when using other email, please report it on github issue)

With android:

(After generating the file "`You_timetable.ics`")

(Using google calendar as an example)

1. Open the website of Google calendar. https://calendar.google.com/calendar
2. click "`setting`" - "`setting`"(at the right-top of this page)
![](https://github.com/FT1ger/fcalendar/blob/main/images/setings.png)
3. Find "`Import and Export`" at the left.
![](https://github.com/FT1ger/fcalendar/blob/main/images/import.png)
4. Import "`You_timetable.ics`"

## Problems

- Haven't been tested with android.
- Potential errors inside.

(Please feed back any bug on github issue)

## Steps

- [x] Import .eml file
- [x] Read datas from email(.eml)
- [x] Catch some specific words to get datas
- [x] Put every data in right place with write form of .ics file
- [x] Output the .ics file.
- [ ] Pythonize
- [x] Remove numpy
- [x] and pandas
- [x] Remove icalendar
- [ ] UI
