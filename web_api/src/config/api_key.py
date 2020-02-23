import os


class ApiKeySettings:
    ''' Api-Key Settings
    '''
    API_KEY = os.environ.get('API_KEY')

    def __init__(self):
        self._validate_api_key()

    def _validate_api_key(self):
        if self.API_KEY is None:
            raise ValueError("API_KEY should not be empty")
