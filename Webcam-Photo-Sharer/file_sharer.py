from filestack import Client


class FileSharer:

    def __init__(self, filepath, api_key="AViVqp7suSQWWEdrl6hf9z"):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        file_link = client.upload(filepath=self.filepath)
        return file_link.url
