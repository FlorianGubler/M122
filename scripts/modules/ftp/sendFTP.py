from ftplib import FTP
import time
import logging

def send_ftp(config, reportFile, FTPPassword):
    logging.info("Start uploading report via FTP")
    ftp = FTP(config['host'])
    ftp.login(config['user'], FTPPassword)
    ftp.cwd(config['uploadDir'])
    filename = "report_" + str(time.time()) + ".pdf"
    ftp.storbinary('STOR ' + filename, open(reportFile, 'rb'))
    logging.info("Uploaded Report via FTP succesfully to '" + config['uploadDir'] + filename + "'")
