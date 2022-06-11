class drive(object):
    def __init__(self, client: object):
        self.service = client
    
    def get_all_files(self, query: str = None) -> list:
        """
        get_all_files allows a user to get a list of files from the drive of which the API has access to.
        :param query: The query to use to get the files.
        :return: A list of files.
        """
        try:
            if query is None:
                return self.service.files().list().execute()
            else:
                return self.service.files().list(q=query).execute()
        except Exception as e:
            raise e
    
    def get_file(self, file_id: str) -> object:
        """
        get_file allows a user to get a file from the drive.
        :param file_id: The id of the file to get.
        :return: A file.
        """
        try:
            return self.service.files().get(fileId=file_id).execute()
        except Exception as e:
            raise e
    
    def create_file(self, file_name: str, mime_type: str, parents: list = None) -> object:
        """
        create_file allows a user to create a file in the drive.
        :param file_name: The name of the file to create.
        :param mime_type: The mime type of the file to create.
        :param parents: The parents of the file to create.
        :return: A file.
        """
        # TODO - Fix this to be able to create a file
        try:
            if parents is None:
                return self.service.files().create(body={'name': file_name, 'mimeType': mime_type}).execute()
            else:
                return self.service.files().create(body={'name': file_name, 'mimeType': mime_type, 'parents': parents}).execute()
        except Exception as e:
            raise e