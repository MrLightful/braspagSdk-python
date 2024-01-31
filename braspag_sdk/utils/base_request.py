import json
import uuid
from typing import Dict

from future.utils import raise_with_traceback
from requests import Request, Session

from braspag_sdk import ObjectJSON
from braspag_sdk.apps.payments.data import MerchantCredentials


class Base(object):

    def __init__(self, authorization_headers: Dict):
        self.authorization_headers = authorization_headers

    def send_request(self, method, uri, data=None, params=None):

        s = Session()

        body = data

        headers = {
            'User-Agent': "BraspagSdk/Python",
            'RequestId': str(uuid.uuid4()),
            **(self.authorization_headers or {}),
        }

        if not body:
            headers['Content-Length'] = '0'
        elif isinstance(data, ObjectJSON):
            body = body.toJSON()

        if 'Content-Type' not in headers:
            headers["Content-Type"] = "application/json"

        req = Request(method, uri, data=body, headers=headers, params=params)

        prep = s.prepare_request(req)

        response = s.send(prep)

        if 'json' in response.headers.get('Content-Type', '').lower():
            answers = response.json()
        else:
            answers = [{
                'Code': str(response.status_code),
                'Message': response.text
            }]

        if response.status_code >= 400:
            data_send = body
            if not isinstance(data_send, dict):
                data_send = json.loads(data_send or 'null')
            raise_with_traceback(Exception(
                '\r\n%s\r\n'
                'Method: %s\r\n'
                'Uri: %s\r\n'
                'Data: %s' % (response.content, method, response.url, json.dumps(data_send, indent=2))
            ))

        return answers


class ApiBase(Base):

    def __init__(self, credentials: MerchantCredentials):
        authorization_headers = {
            'MerchantId': credentials.merchant_id,
            'MerchantKey': credentials.merchant_key,
        }
        super().__init__(authorization_headers=authorization_headers)


class ApiOauthBase(Base):

    def __init__(self, access_token: str):
        authorization_headers = {
            'Authorization': 'Bearer ' + access_token,
        }
        super().__init__(authorization_headers=authorization_headers)
