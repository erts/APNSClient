# push.py 
#
# simple script for sending a test push notification message to device over APNs
# https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CreatingtheNotificationPayload.html#//apple_ref/doc/uid/TP40008194-CH10-SW1


 
import apns2

DEVICE_TOKEN = ""


def push(self, device_token = DEVICE_TOKEN):
    """ send push message to iOS device over APNs"""
    client = apns2.APNSClient(mode = "dev", client_cert = "certs/apns-dev-cert.pem")
    alert = apns2.PayloadAlert(body = "some alert content", title = "an alert title")
    payload = apns2.Payload(alert = alert, content_available = True)
    notification = apns2.Notification(payload = payload, priority = apns2.PRIORITY_LOW)
    response = client.push(n = notification, device_token = device_token)
    
    print('{0} - {1}, {2}, {3} '.format(response.timestamp response.reason, response.status_code, response.apns_id)) 


push()