from os import environ

from google.cloud import storage

bucket_name = environ.get('FLASH_STORAGE')

class GoogleStorage:
    def __init__(self):
        storage_client = storage.Client()
        self.bucket = storage_client.bucket(bucket_name)

    def upload(self,file_name,destination):
        """Uploads a file to the bucket."""
        blob = self.bucket.blob(destination)
        blob.upload_from_filename(file_name)
