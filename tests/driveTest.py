import sys
sys.path.insert(1, '../pythonDrive')
import auth
import drive

secretKey: str = 'secretFiles/auth.json'

def test_auth():
    try:
        client = auth.clientServiceAccountAuth(secretKey, ['https://www.googleapis.com/auth/drive'])
        assert client is not None
    except Exception as e:
        raise e

def test_auth_creds():
    try:
        credentials = auth.credsServiceAccountAuth(secretKey, ['https://www.googleapis.com/auth/drive'])
        assert credentials is not None
    except Exception as e:
        raise e

def test_drive():
    try:
        client = auth.clientServiceAccountAuth(secretKey, ['https://www.googleapis.com/auth/drive'])
        thisDrive = drive.drive(client)
        assert thisDrive is not None
    except Exception as e:
        raise e

def test_drive_get_all_files():
    try:
        client = auth.clientServiceAccountAuth(secretKey, ['https://www.googleapis.com/auth/drive'])
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