
import boto3
import datetime
import json
import logging
import socket
import ssl

# sns = boto3.client('sns')
# cloudfront = boto3.client('cloudfront')

# logger = logging.getLogger()
# logger.setLevel(logging.INFO)

hostname='google.com'
class AlreadyExpired(Exception):
    pass

def ssl_expiry_datetime(hostname):
    ssl_date_fmt = r'%b %d %H:%M:%S %Y %Z'

    context = ssl.create_default_context()
    conn = context.wrap_socket(
        socket.socket(socket.AF_INET),
        server_hostname=hostname,
    )
    # 3 second timeout because Lambda has runtime limitations
    conn.settimeout(3.0)

    conn.connect((hostname, 443))
    ssl_info = conn.getpeercert()
    # parse the string from the certificate into a Python datetime object
    return datetime.datetime.strptime(ssl_info['notAfter'], ssl_date_fmt)

def ssl_valid_time_remaining(hostname):
    expires = ssl_expiry_datetime(hostname)
    logger.debug(
        "SSL cert for %s expires at %s",
        hostname, expires.isoformat()
    )
    return expires - datetime.datetime.utcnow()
    
    my_dict = {'date': (expires- datetime.datetime.now())}

#print(json.dumps(ssl_expiry_datetime)
