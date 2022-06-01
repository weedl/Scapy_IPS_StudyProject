import os
import shutil

def new_log():
    f = open('incident_report.txt', 'w')
    f.write('')
    f.close()
    # this block of code will wipe the file - making it ready for a new period of reporting

def write():
    f = open('incident_report.txt', 'a')
    f.write('This is an incident with code 404\n') # insert whatever shall be written to the file once an incident occurs here
    f.close()

def cplog():
    report = r'incident_report.txt'
    log = r'path to log file'

    # this blcok of code is supposed to copy the content of the incident report txt file, and write it to a log directory. The log
    # directory is supposed to be organized by date and time of the report. For instance the 08:00 report will be marked with:
    # 08 - dd.mm.yyyy
