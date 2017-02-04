#### Import-SSU-schedule-to-Google-Calendar

##### Requirements:

* google-api-python lib
    * For install: `pip install --upgrade google-api-python-client`
* Python 3.5 or greater

##### How to use it:

* First of all you should generate `client_secret.json` for it read `Step 1: Turn on the Google Calendar API`  [HERE](https://developers.google.com/google-apps/calendar/quickstart/python). 
* Put json file to folder with this scripts
* run `main.py`
   * when main.py will running you are able to see: 
      * `[INFO] Event created: LINK1`
      * `[INFO] Event created: LINK2`
      * `[INFO] Event created: LINK3`
      * `...`
   * The schedule will be added starting next Monday.