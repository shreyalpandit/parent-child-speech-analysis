from __future__ import print_function
import time
import deepaffects
from deepaffects.rest import ApiException
from pprint import pprint

# Configure API key authorization: UserSecurity
deepaffects.configuration.api_key['apikey'] = 'YOUR_API_KEY'
# create an instance of the API class
api_instance = deepaffects.DenoiseApi()
audio = deepaffects.Audio.from_file('/path/to/file') # Audio | Audio object that needs to be denoised.
