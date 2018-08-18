import requests

from fandogh_cli.fandogh_client import base_url, get_exception, _parse_key_values
from fandogh_cli.fandogh_client import get_stored_token

base_secrets_url = '%ssecrets' % base_url


def list_secret(secret_type):
    token = get_stored_token()
    response = requests.get("{}?secret_type={}".format(base_secrets_url, secret_type),
                            headers={'Authorization': 'JWT ' + token})
    if response.status_code != 200:
        raise get_exception(response)
    else:
        return response.json()


def create_secret(name, secret_type, fields):
    token = get_stored_token()
    response = requests.post(base_secrets_url,
                             headers={'Authorization': 'JWT ' + token},
                             json={
                                 "name": name,
                                 "type": secret_type,
                                 "fields": _parse_key_values(fields)
                             },
                             )
    if response.status_code != 200:
        raise get_exception(response)
    else:
        return response.json()