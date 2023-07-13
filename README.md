# Weekly Sport Report (TBZ M122 LB2)

## Installation
For installation, the complete Repository 'M122' has to be cloned / downloaded, to the wished enviromnent. After that you have to checkout the branch 'florian' to get the state of the project, this docs are made for. You can do this using following commands:
```bash
cd M122/
git checkout florian
```
After that, we need to specify the credentials, the script can use. For that we need to create a <code>cred.yml</code> file out of the repository directory. The file needs to be one layer on top of this directory:
```
.
├── M122
│   ├── .git
│   ├── .gitignore
│   ├── README.md
│   └── src
└── cred.yml
```
You can do this using these commands:
```bash
cd ../
touch cred.yml
```
Now, of course, you also need to specify the credentials in the file. The file structure should look as following (For using our servers, make an email to gubler.florian@gmx.net to request the credentials):
```yaml
apikeys:
  nba: "xxx"
  football: "xxx"
mail:
  password: "xxx"    
ftp:
  password: "xxx"
```
After that we have to install the required python and system libraries. To use this script, the following packages are required:
### System libraries:
- python3.8 or higher (When not already installed)
- wkhtmltopdf
### Python packages:
- pdfkit
- PyYaml
- ftlib
- traceback <i>(Mostly default installed)</i>
- email <i>(Mostly default installed)</i>
- smtplib <i>(Mostly default installed)</i>
- logging <i>(Mostly default installed)</i>
- time / datetime <i>(Mostly default installed)</i>
Lastly we have to install the weekly cronjob. Using following command, you can see the configured cronjobs.
```bash
crontab -e
```
This opens a file with a list of the configured cronjobs. Take the following configuration for the weekly sport report script cronjob, configure it correctyl and put it into the opened crontab config file after the comments on top of the page:
```bash
MAILTO=<YOUR-IT-ADMIN-EMAIL>
@weekly cd <INSTALLATION-PATH>/M122/src/ && ./main.py >> ./logs/m122_cron.log 2>&1
```
<b>Now your setup is finished!</b>

:exclamation: If your using a different config, than the main one you have to specify this in the file <code>src/config/config.yml</code>.
<br>
## Instruction manual for endusers
If your an enduser of this script, you usally don't have to do much. The sport report script is sheduled and runs every week, to get you updated. The standard mail sender of the script configured is m122.testmail@gmail.com. If you want to configure something else, just like the receivers of the script, the subject, etc. The configuration file is located in <code>src/config/config.yml</code>.
<br>
### Errormail
If you receive an error mail, that something in the script went wrong, please contact you IT administrator. Such mail has the subject 'Error in Sport Report Script' and contains some additional info from the error. 
<br>
### Start the script manually
If you sometime want to run the script manually and don't wait another week, you can do this just by calling the following:
```bash
./src/main.yml
```
<br>

## Docs for developers
If your a developer or it administrator, it is helpful to underestand, how this sript works. In case of a bug or you want to develop an extra feature, you know how to integrate it into this script. The script has following structure:
```
src/
├── config -> Contains config.yml with the complete script configuration
├── logs -> The logs folder containing m122.log (Script log) and m122_cron.log (Cronjob Log)
├── main.py -> The main script itself
├── modules -> Contains all custom modules for the script 
├── templates -> Contains 3 Templates: mail.html (The report mail), errormail.html (The error mail) and report.html (The pdf template for the report)
└── tmp -> The tmp folder for the script (PDF Report will be stored temporarly be stored there)
```
The configuration file for the credentials is not in the repository folder, but one layer on top as file <code>cred.yml</code>.
### Logging and errorhandling
The logging is configured globaly to write into the logging file. You just have to use the logging module with <code>logging.info() | logging.error() | ...</code>. You can specify the Log Level in main.yml with the Variable <code>LOG_LEVEL</code>. Errors are catched from the main process in the main.yml File and will be logged and sent as an error mail. 

### Current modules
Currently the following modules, are develeoped:
```
src/modules/
├── api                --> The modules for the sport apis, to load the data
│   ├── football.py    --> * The football api module
│   └── nba.py         --> * The nba api modules
├── config.py          --> The module to load the config file of the script
├── ftp                --> The module to handle FTP report sending
│   └── sendFTP.py
├── mail               --> The module to handle Mail report and error sending
│   └── manageMail.py
└── pdf                --> The module to handle the pdf generation
    └── reportPDF.py
```
