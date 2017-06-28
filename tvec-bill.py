import os
from datetime import datetime, timedelta
from twilio.rest import Client
import numpy as np
import requests

def text_estimated_bill(twilio_account, twilio_token, estimated_bill_amount, to_number, from_number):

    client = Client(twilio_account, twilio_token)

    message = client.messages.create(
        to=to_number,
        from_=from_number,
        body="Your estimated bill for the month will be ${}".format(str(estimated_bill_amount))
    )

def tvec_login(session, user, password):

    url = "https://billing.tvec.net/oscp/OnlineServices/FeaturesLogin/tabid/123/Default.aspx"

    payload = {
        'AppID': 'OSCP',
        'ScriptManager': 'dnn%24ctr564%24FeatureLogin%24UpdatePanel1%7Cdnn%24ctr564%24FeatureLogin%24btnLogin',
        'ScriptManager_TSM': '%3B%3BSystem.Web.Extensions%2C%20Version%3D4.0.0.0%2C%20Culture%3Dneutral%2C%20PublicKeyToken%3D31bf3856ad364e35%3Aen%3A209d1e34-0637-48d5-a3e4-55a42f794d73%3Aea597d4b%3Ab25378d2%3BAjaxControlToolkit%2C%20Version%3D1.0.20229.33324%2C%20Culture%3Dneutral%2C%20PublicKeyToken%3D28f01b0e84b6d53e%3Aen%3Af949cc8b-abae-4009-a4c8-0b7c0c356732%3Ab14bb7d5%3A13f47f54%3A1d056c78%3A3c55b13e%3Adc2d6e36%3Ade51bc8f%3Aa3e10fa2%3A701e375f%3Aa4313c7a',
        'ScrollTop': '',
        'StylesheetManager_TSSM': '',
        '__ASYNCPOST': 'true',
        '__EVENTARGUMENT': '',
        '__EVENTTARGET': '',
        '__LASTFOCUS': '',
        '__VIEWSTATE': '%2FwEPDwUJNzA3MDMwMDUzD2QWCGYPFgIeBFRleHQFeTwhRE9DVFlQRSBodG1sIFBVQkxJQyAiLS8vVzNDLy9EVEQgWEhUTUwgMS4wIFRyYW5zaXRpb25hbC8vRU4iICJodHRwOi8vd3d3LnczLm9yZy9UUi94aHRtbDEvRFREL3hodG1sMS10cmFuc2l0aW9uYWwuZHRkIj5kAgIPFgIfAAVDIHhtbDpsYW5nPSJlbi1VUyIgbGFuZz0iZW4tVVMiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sImQCBA9kFg4CBg8WAh4HVmlzaWJsZWhkAgcPFgIeB2NvbnRlbnQFT1RoaXMgVGFiIGlzIGN1cnJlbnRseSBiZWluZyB1c2VkIHRvIGxvZ2luIHRoZSB1c2VyIHRvIHByb3ZpZGUgdmFyaW91cyBmZWF0dXJlcy5kAggPFgIfAgVEbG9naW4gZm9yIHZhcml1b3MgZmVhdHVyZXMgYXZhaWxhYmxlIGluIEJQUCBhbmQgT1NDUC4sRG90TmV0TnVrZSxETk5kAgkPFgIfAgUoQ29weXJpZ2h0IDIwMDkgYnkgRG90TmV0TnVrZSBDb3Jwb3JhdGlvbmQCCg8WAh8CBQtEb3ROZXROdWtlIGQCCw8WAh8CBR5PbmxpbmUgU2VydmljZSBDdXN0b21lciBQb3J0YWxkAg4PFgIfAgUNSU5ERVgsIEZPTExPV2QCBg9kFgJmD2QWAgIHD2QWAmYPZBYSZg9kFgICAQ8WAh4FY2xhc3MFKkRubk1vZHVsZSBEbm5Nb2R1bGUtRE5OX0hUTUwgRG5uTW9kdWxlLTUxOBYCAgEPZBYCZg9kFgICAQ8PZBYCHwMFHEROTk1vZHVsZUNvbnRlbnQgTW9kRE5OSFRNTENkAgEPFgIeBGhyZWYFQ2h0dHBzOi8vYmlsbGluZy50dmVjLm5ldC9vc2NwL09ubGluZVNlcnZpY2VzL3RhYmlkLzEyNC9EZWZhdWx0LmFzcHhkAgIPFgIfBAU%2BaHR0cHM6Ly9iaWxsaW5nLnR2ZWMubmV0L29zY3AvQ29udGFjdFVzL3RhYmlkLzIzOS9EZWZhdWx0LmFzcHhkAgMPZBYCAgEPFgIfAwUqRG5uTW9kdWxlIERubk1vZHVsZS1ETk5fSFRNTCBEbm5Nb2R1bGUtNTI4FgICAQ9kFgJmD2QWAgIBDw9kFgIfAwUcRE5OTW9kdWxlQ29udGVudCBNb2RETk5IVE1MQ2QCCQ9kFgRmDw8WCh4IQ3NzQ2xhc3MFCkJyZWFkY3J1bWIfAGUeB1Rvb2xUaXBlHgtOYXZpZ2F0ZVVybAWcAWh0dHBzOi8vYmlsbGluZy50dmVjLm5ldC9vc2NwL0N1c3RvbWVyTG9naW4vdGFiaWQvMTIzL2N0bC9Mb2dpbi9EZWZhdWx0LmFzcHg%2FcmV0dXJudXJsPSUyZm9zY3AlMmZPbmxpbmVTZXJ2aWNlcyUyZkZlYXR1cmVzTG9naW4lMmZ0YWJpZCUyZjEyMyUyZkRlZmF1bHQuYXNweB4EXyFTQgICFgIeB29uY2xpY2sF1gFyZXR1cm4gZG5uTW9kYWwuc2hvdygnaHR0cHM6Ly9iaWxsaW5nLnR2ZWMubmV0L29zY3AvQ3VzdG9tZXJMb2dpbi90YWJpZC8xMjMvY3RsL0xvZ2luL0RlZmF1bHQuYXNweD9yZXR1cm51cmw9L29zY3AvT25saW5lU2VydmljZXMvRmVhdHVyZXNMb2dpbi90YWJpZC8xMjMvRGVmYXVsdC5hc3B4JnBvcFVwPXRydWUnLC8qc2hvd1JldHVybiovdHJ1ZSwzMDAsNjUwLHRydWUsJycpZAICDxYCHwFoFgICAQ8PFgofBQUKQnJlYWRjcnVtYh8AZR8GZR8HBZwBaHR0cHM6Ly9iaWxsaW5nLnR2ZWMubmV0L29zY3AvQ3VzdG9tZXJMb2dpbi90YWJpZC8xMjMvY3RsL0xvZ2luL0RlZmF1bHQuYXNweD9yZXR1cm51cmw9JTJmb3NjcCUyZk9ubGluZVNlcnZpY2VzJTJmRmVhdHVyZXNMb2dpbiUyZnRhYmlkJTJmMTIzJTJmRGVmYXVsdC5hc3B4HwgCAhYCHwkF1gFyZXR1cm4gZG5uTW9kYWwuc2hvdygnaHR0cHM6Ly9iaWxsaW5nLnR2ZWMubmV0L29zY3AvQ3VzdG9tZXJMb2dpbi90YWJpZC8xMjMvY3RsL0xvZ2luL0RlZmF1bHQuYXNweD9yZXR1cm51cmw9L29zY3AvT25saW5lU2VydmljZXMvRmVhdHVyZXNMb2dpbi90YWJpZC8xMjMvRGVmYXVsdC5hc3B4JnBvcFVwPXRydWUnLC8qc2hvd1JldHVybiovdHJ1ZSwzMDAsNjUwLHRydWUsJycpZAILDw8WAh8BZ2RkAg4PFgIfAwUMRE5ORW1wdHlQYW5lZAIPD2QWBAIBDxYCHwMFPERubk1vZHVsZSBEbm5Nb2R1bGUtQ3VzdG9taXphdGlvbnNGZWF0dXJlTG9naW4gRG5uTW9kdWxlLTU2NBYCAgEPZBYCZg8WAh8DBQ5ETk5BbGlnbmNlbnRlchYCAgEPD2QWAh8DBS9ETk5Nb2R1bGVDb250ZW50IE1vZEN1c3RvbWl6YXRpb25zRmVhdHVyZUxvZ2luQxYCAgEPDxYCHgtmZWF0dXJlTmFtZQUKTWV0ZXJVc2FnZWQWAmYPZBYCZg9kFhACCw8PFgIfAWhkZAINDw8WAh8BaGRkAg8PDxYCHwFoZGQCEQ8PFgIfAWhkZAITDw8WAh4NT25DbGllbnRDbGljawUScmV0dXJuIFZhbGlkYXRlKCk7ZGQCGQ8PFgIfBwVZaHR0cHM6Ly9iaWxsaW5nLnR2ZWMubmV0L29zY3AvTXlBY2NvdW50L0NyZWF0ZVVzZXJJZC9DcmVhdGVOZXdVc2VyL3RhYmlkLzE5MC9EZWZhdWx0LmFzcHhkZAIbDw8WAh8HBVpodHRwczovL2JpbGxpbmcudHZlYy5uZXQvb3NjcC9NeUFjY291bnQvQ3JlYXRlVXNlcklkL0ZvcmdvdFBhc3N3b3JkL3RhYmlkLzE5NC9EZWZhdWx0LmFzcHhkZAIhDw9kFgIfCQVfd2luZG93LnRvcC5sb2NhdGlvbi5ocmVmPSdodHRwczovL2JpbGxpbmcudHZlYy5uZXQvb3NjcC9PbmxpbmVTZXJ2aWNlcy90YWJpZC8xMjQvRGVmYXVsdC5hc3B4JztkAgIPFgIfAwUqRG5uTW9kdWxlIERubk1vZHVsZS1ETk5fSFRNTCBEbm5Nb2R1bGUtNTY5FgICAQ9kFgJmD2QWAgIBDw9kFgIfAwUcRE5OTW9kdWxlQ29udGVudCBNb2RETk5IVE1MQ2QCEA8WAh8DBQxETk5FbXB0eVBhbmVkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYCBQppbWdBbmRyb2lkBQZpbWdpT1PJkuD2jv5zUi4C6cTWzUcG9phC3g%3D%3D',
        '__VIEWSTATEGENERATOR': 'F462CD71',
        '__dnnVariable': '%60%7B%60__scdoff%60%3A%601%60%2C%60sf_siteRoot%60%3A%60%2Foscp%2F%60%2C%60sf_tabId%60%3A%60123%60%7D',
        'dnn%24ctr564%24FeatureLogin%24btnLogin': 'Login',
        'dnn%24ctr564%24FeatureLogin%24hdnLoginCaptchaIsEnabled': 'false',
        'dnn%24ctr564%24FeatureLogin%24txtPassword': password,
        'dnn%24ctr564%24FeatureLogin%24txtUsername': user,
        'hidEnableRedirection': 'true',
        'hidParam484': '1',
        'hidSmartApp': '0'
    }
    headers = {
        'origin': "https://billing.tvec.net",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "en-US,en;q=0.8",
        'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
        'accept': "*/*",
        'cache-control': "no-cache",
        'x-requested-with': "XMLHttpRequest",
        'connection': "keep-alive",
        'x-microsoftajax': "Delta=true",
        'referer': "https://billing.tvec.net/oscp/OnlineServices/FeaturesLogin/tabid/123/Default.aspx"
    }

    response = session.post(
        url,
        data="&".join(["=".join(x) for x in payload.items()]),
        headers=headers
    )
    return session

def dailyUsage(session, tvec_member_number):

    url = "https://billing.tvec.net/oscp/DesktopModules/MeterUsage/API/MeterData.aspx/GetDailyUsageData"
    today = datetime.now().strftime("%m/%d/%Y")
    month_ago = (datetime.now() - timedelta(days=31)).strftime("%m/%d/%Y")
    json = {
        "MemberSep": tvec_member_number,
        "StartDate": month_ago,
        "EndDate": today,
        "IsEnergy":"true",
        "IsPPM":"false",
        "IsCostEnable":"1"
    }

    headers = {
        'origin': "https://billing.tvec.net",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "en-US,en;q=0.8",
        'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        'content-type': "application/json; charset=UTF-8",
        'accept': "application/json, text/javascript, */*; q=0.01",
        'referer': "https://billing.tvec.net/oscp/MyAccount/AccountHistory/UsageHistory/MeterUsageList/tabid/266/Default.aspx",
        'x-requested-with': "XMLHttpRequest",
        'connection': "keep-alive",
        'cache-control': "no-cache",
    }
    response = session.post(
        url,
        json=json,
        headers=headers
    )
    return response.json()


def lambda_handler(event, context):
    session = requests.session()
    response = session.get("https://billing.tvec.net/oscp/")
    
    session = tvec_login(
        session,
        os.environ['tvec_user'],
        os.environ['tvec_password']
    )

    usage = dailyUsage(
        session,
        os.environ['tvec_member_number']
    )
    daily_usages = np.array(
        [
            int(x['TOTALENERGY'])
            for x
            in usage['d']['Items']
            if x['TOTALENERGY'] != "NaN"
        ]
    )
    text_estimated_bill(
        os.environ['twilio_account'],
        os.environ['twilio_token'],
        daily_usages.mean() * 31 * .12,
        os.environ['to_number'],
        os.environ['twilio_number']
    )
lambda_handler(1, 1)
