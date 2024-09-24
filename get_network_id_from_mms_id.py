import urllib.request
from lxml import etree
import pandas as pd
import re

'''
Python script für das Ergänzen der Network ID aus einer Exceldatei mit MMS ID.
Die Input-Datei muss mindestens eine Spalte namens "MMS ID" mit gültigen MMS ID der Institution Zone enthalten. 
Das Script ergänzt die Datei mit einer Spalte "Network ID" mit der entsprechenden NZ ID (oder bei CZ records, die CZ ID). Wenn keine NZ oder CZ ID gefunden wird, bleibt die Spalte leer.
Der Name der Inputdatei muss angepasst werden bevor das Script läuft (Variable "input_file).
'''

# File name
input_file = "inputfile.xlsx" # change the name of your input file here

# SRU base and namespaces:
sru = 'https://slsp-rzs.alma.exlibrisgroup.com/view/sru/41SLSP_RZS?version=1.2&operation=searchRetrieve&recordSchema=marcxml&query=rec.id=' # MARC: Alma SRU Base URL for IZ RZS
ns = {'xmlns' : 'http://www.loc.gov/zing/srw/', 
  'slim' : 'http://www.loc.gov/MARC21/slim'}  


def getBibFromSRU(recid, ns, sru):
    sruUrl = sru+recid

    #Initial SRU-Request        
    root = etree.parse(urllib.request.urlopen(sruUrl))
    #Initial xpath to parse the first  records
    record = root.findall(".//xmlns:record",ns)

    #Get the nextRecordValue to build the further SRU-Requests with additional startRecord URI-Parameter
    nextRecord = root.find(".//xmlns:nextRecordPosition",ns)
    
    return record


def get_nz_id(record, ns):
    for rec in record:

        try:
            exlibrisID = rec.xpath(".//slim:datafield[@tag='035']/slim:subfield[@code='a'][starts-with(text(),'(EXL')]",namespaces=ns)
            print(exlibrisID[0].text)
            match = re.search(r'\)\d+', exlibrisID[0].text) # search for the closing bracket ')'
            if match:    # Return just the ID without the Brackets
                network_id = match.group(0)[1:]  # First position is ')', therefore [1:]
                return network_id
            else:
                print("-------------------------------------------------------------------------no match for ')' in field 035 !")
                return None
        except:
            print("*****************************************************************************no Network or Community zone ID found in MARC field 035!")
            return None

        
 
    
# Read the Excel file into a pandas DataFrame
df = pd.read_excel(input_file)
df['MMS ID'] = df['MMS ID'].astype(str)
df["Network ID"] = None

for idx, row in df.iterrows():

    mms_id = row['MMS ID']
    print(mms_id)
    sruRecord = getBibFromSRU(mms_id, ns, sru)
    nz_id = get_nz_id(sruRecord, ns)
    print(nz_id)
    df.loc[idx, 'Network ID'] = nz_id


#print(df)
df.to_excel(input_file, index=False)
print("File saved:", input_file)
