import requests
import datetime
from requests.auth import HTTPDigestAuth



def getImageFromCamera():
    url = 'http://{url}/ISAPI/Streaming/channels/101/picture?snapShotImageType=JPEG'.format(url="192.168.30.159")
    r = requests.get(url, auth=HTTPDigestAuth('admin', 'Admin12345'), stream=True)
    if r.status_code == 200:
        with open("sample.jpg", 'wb') as f:
            f.write(r.content)




if __name__ == '__main__':
    getImageFromCamera()