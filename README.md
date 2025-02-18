# FCalendar
FCalendar is a small tool for student in the University of Adelaide which can read your schedule from email and generate an iCalandar (.ics) file, which can be imported to your Calendar app.

## Dependencies
Make sure that you have installed those libraries:
- pandas
- numpy
- icalendar

## How can I use FCalendar

1. Open your Timetable Planner.(https://access.adelaide.edu.au/sa/student/TimeTablePlanner.asp)
2. Generate your Timetable.
3. View it.
4. Click the "Email" button (at the left-top of this page).
5. Send it to your email.
6. Download the email file and place it in the same directory of `FCalendar.py`.(Its name should be "`Your Potential Timetable.eml`")
7. Run FCalendar.py
8. Generate a file "`Your_timetable.ics`", send it to your phone or import it to your calendar app.

(If you are using iOS, strongly advise you create a new calendar to manage all the events.)

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
- [ ] Remove numpy and pandas
- [ ] Remove icalendar
- [ ] UI
