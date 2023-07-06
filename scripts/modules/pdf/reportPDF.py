import pdfkit

def generatePDFReport(CONFIG, APIDATA):
    with open(CONFIG['template'], "r") as file:
        content = file.read()

        # Football
        content = content.replace("%%FOOT_NAME%%", APIDATA['football']['response'][0]['player']['name'])
        content = content.replace("%%FOOT_CLUB%%", APIDATA['football']['response'][0]['statistics'][0]['team']['name'])  
        content = content.replace("%%FOOT_COUNT%%", str(APIDATA['football']['response'][0]['statistics'][0]['goals']['total']))  

        # NBA
        content = content.replace("%%NBA_NAME%%", APIDATA['nba'][0]['player']['knownName'])  
        content = content.replace("%%NBA_CLUB%%", APIDATA['nba'][0]['team']['name'])  
        content = content.replace("%%NBA_COUNT%%", str(APIDATA['nba'][0]['pointsPerGame']))  

        # Generate PDF
        pdfkit.from_string(content, CONFIG['tmpfile'])
