"""
pip install pythonDrive
"""
# import pythondrive
from pythonDrive import auth as pyAuth
from pythonDrive import drive as pyDrive


def test_pip_auth():
    """
        test_pip_auth():
        param: None
        return: None
        test_pip_auth() is responsible for testing the auth.py module from pip
    """
    try:
        client = pyAuth.clientServiceAccountAuth('secretFiles/auth.json', ['https://www.googleapis.com/auth/drive'])
        assert client is not None
        print("done")
    except Exception as e:
        raise e

def test_pip_auth_creds():
    """
        test_pip_auth_creds():
        param: None
        return: None
        test_pip_auth_creds() is responsible for testing the auth module but returning credentials from pip
    """
    try:
        credentials = pyAuth.credsServiceAccountAuth('secretFiles/auth.json', ['https://www.googleapis.com/auth/drive'])
        assert credentials is not None
        print("done")
    except Exception as e:
        raise e

def test_pip_drive():
    """
        test_pip_drive():
        param: None
        return: None
        test_pip_drive() is responsible for testing the drive.py module from pip
    """
    try:
        client = pyAuth.clientServiceAccountAuth('secretFiles/auth.json', ['https://www.googleapis.com/auth/drive'])
        thisDrive = pyDrive.drive(client)
        assert thisDrive is not None
        print("done")
    except Exception as e:
        raise e

if __name__ == '__main__':
    test_pip_auth()
    test_pip_auth_creds()
    test_pip_drive()
    