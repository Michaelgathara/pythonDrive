import sys
# sys.path.insert(1, '../pythonDrive')
from pythonDrive import auth
from pythonDrive import drive

test_secretKey: str = 'secretFiles/auth.json'

def test_auth():
    """
        test_auth():
        param: None
        return: None
        test_auth() is responsible for testing the auth.py module
    """
    try:
        client = auth.clientServiceAccountAuth(test_secretKey, ['https://www.googleapis.com/auth/drive'])
        assert client is not None
    except Exception as e:
        raise e

def test_auth_creds():
    """
        test_auth_creds():
        param: None
        return: None
        test_auth_creds() is responsible for testing the auth module but returning credentials
    """
    try:
        credentials = auth.credsServiceAccountAuth(test_secretKey, ['https://www.googleapis.com/auth/drive'])
        assert credentials is not None
    except Exception as e:
        raise e

def test_drive():
    try:
        client = auth.clientServiceAccountAuth(test_secretKey, ['https://www.googleapis.com/auth/drive'])
        thisDrive = drive.drive(client)
        assert thisDrive is not None
    except Exception as e:
        raise e

def test_drive_get_all_files():
    try:
        client = auth.clientServiceAccountAuth(test_secretKey, ['https://www.googleapis.com/auth/drive'])
        thisDrive = drive.drive(client)
        listOfFiles: list = thisDrive.get_all_files()
        print(listOfFiles)
        assert listOfFiles is not None
    except Exception as e:
        raise e

if __name__ == '__main__':
    test_auth()
    test_auth_creds()
    test_drive()
    test_drive_get_all_files()