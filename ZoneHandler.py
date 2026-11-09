import requests
from bs4 import BeautifulSoup

class ZoneHandler:
    FEATURE_NAMESPACE = "dipul"
    REQUEST_URL = "https://uas-betrieb.de/geoservices/dipul/ows"

    def getFeature(self, feature_name: str):
        params: dict = {
            "service": "WFS",
            "version": "2.0.0",
            "request": "GetFeature",
            "typenames": self.FEATURE_NAMESPACE + ":" + feature_name,
        }

        try:
            response = requests.get( self.REQUEST_URL, params)
            response.raise_for_status()
            return response.text, None
        except requests.RequestException as e:
            detail = e.response.text if e.response is not None else "No Body"
            return None, f"{e} - {detail}"


    def save_as_xml(self, text: str):
        xml_data = BeautifulSoup(text, 'xml')
        open(f"data/zones/{zone_name}.xml","x").write(xml_data.prettify())


zonehandler = ZoneHandler()
zone_name = "flugplaetze"

data, error = zonehandler.getFeature(zone_name)

if(error):
    print(error)
    
if(data):
    zonehandler.save_as_xml(data)