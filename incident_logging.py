import os
import shutil
import subprocess

def new_log(date):
    f = open('incident_report.txt' + date, 'w')
    f.write('')
    f.close()
    # this block of code will wipe the file - making it ready for a new period of reporting

def write(date):
    f = open('incident_report.txt' + date, 'a')
    f.write('This is an incident with code 404\n') # insert whatever shall be written to the file once an incident occurs here
    f.close()

def cplog(date):
    report = r'incident_report.txt' + date
    log = r'path to log file' + 'log' + date
    cmd = 'cp'
    
    try:
        copy_report = subprocess.Popen([cmd, report, log] stdout = subprocess.PIPE)
        print(r'Report {} has been logged to the path: {}'.format(report, log)
   
    except:
        print('An error occured while trying to copy {} to destination')
              
              
