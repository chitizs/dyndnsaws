import pycurl
from io import BytesIO 

def find_ip():
    b_obj = BytesIO()
    crl = pycurl.Curl() 
    crl.setopt(crl.URL, 'http://169.254.169.254/latest/meta-data/public-ipv4')
    # Write bytes that are utf-8 encoded
    crl.setopt(crl.WRITEDATA, b_obj)
    crl.perform() 
    crl.close()
    # Get the content stored in the BytesIO object (in byte characters) 
    get_body = b_obj.getvalue()
    #decode byte to string 
    return get_body.decode('utf8')
    
