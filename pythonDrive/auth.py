# Currently only support service_accounts
from google.oauth2 import service_account
from googleapiclient.discovery import build

def clientServiceAccountAuth(file_path: str, scopes: list) -> object:
    """
    clientServiceAccountAuth allows a user to auth with a service account and return a client object that has a built service.
    :param file_path: The path to the service account json file.
    :param scopes: The scopes to request you would like to build the service with, Should be a List of strings.
    :return: A service account object.
    """
    credentials = service_account.Credentials.from_service_account_file(file_path, scopes=scopes)
    try:
        return build('drive', 'v3', credentials=credentials)
    except Exception as e:
        raise e

def credsServiceAccountAuth(file_path: str, scopes: list) -> object:
    """
    credsServiceAccountAuth allows a user to auth with a service account and return the credentials object to perhaps build the service yourself.
    :param file_path: The path to the service account json file.
    :param scopes: The scopes to request you would like to build the service with, Should be a List of strings.
    :return: A service account object.
    """
    credentials = service_account.Credentials.from_service_account_file(file_path, scopes=scopes)
    try:
        return credentials
    except Exception as e:
        raise e