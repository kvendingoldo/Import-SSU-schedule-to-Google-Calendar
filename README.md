### Import-SSU-schedule-to-Google-Calendar

##### How to use it:

* First of all you should generate `client_secret.json` for it read `Step 1: Turn on the Google Calendar API`  [HERE](https://developers.google.com/google-apps/calendar/quickstart/python). 
* Pay attention on the `resources/config.json`. Parameters `path_to_creds`, `personal_email`, `calendarId` should be changed.
* run `main.py`
   * when main.py will running you are able to see: 
      * `[INFO] Event created: LINK1`
      * `[INFO] Event created: LINK2`
      * `...`
   * The schedule will be added starting next Monday.
   

### Configuration:

* Config parameters:
    * `"study_mode"` : can be `do` or `zo`
    * `"department"` : your study department 
    * `"group"` : your study group 

    * Colors parameters like `color.lesson`: You can get color code below(in image). If field is empty will be used `color.default` parameter.
        * examples:
            * `"color.lesson": "5"`
            * `"color.laboratory_work": "9"`
    
    * Specializations: If you have extra subjects you can include them to your calendar by `"include.specializations"`
        * examples:
            * `"include.specializations": "1-C web-дизайн"`
            * `"include.specializations": "перев. 2"`
    
    * Calendar parameters:
        * `"personal_email"` : your personal email which will be added to event. Can be empty.
        * `"recurrence"` : 
        * `"recurrence.freq"` : can be `WEEKLY` or `DAILY`
        * `"recurrence.count"` : count of week
        * `"timezone"`
            * by default used `UTC+4` timezone (`"Europe/Samara"`)

        * `"calendarId"` : calendar for using.
            * by default used `"primary"` which is `your_email@gmail.com` calendar
            * instruction how get `calendarId` [here](https://docs.simplecalendar.io/find-google-calendar-id/)

        * `"reminder.useDefault"` : default google reminders. Can be `True/False`.
        * `"reminder.popup"` : popup behind N minutes
            * example: `"reminder.popup": "20"`
        * `"system.calendar.interval"` : system parameter
        
   
#### Appendix
![google_colors_id](google_colors_id.png)

#### Useful links
[recurring_events API](https://developers.google.com/google-apps/calendar/concepts/events-calendars#recurring_events)
