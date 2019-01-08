import deepaffects
from deepaffects.realtime.util import chunk_generator_from_file, chunk_generator_from_url, get_deepaffects_client


TIMEOUT_SECONDS = 2000
apikey = "3RVW9BCSGBdZxhGZSdwlGe8F9qcLnGtA"

# file = '/Users/shreyalpandit/Dropbox (MIT)/Repos/parent-child-speech-analysis/sample.mp3'

file = 'https://www.youtube.com/watch?v=EdHR3ZMCNBc'

# Set is_youtube_url True while streaming from youtube url
is_youtube_url = True
languageCode = "en-Us"
sampleRate = "16000"
encoding = "wav"
speakerIds = "list of speakerIds to be identified seperated by ','"

# DeepAffects realtime Api client
client = get_deepaffects_client()

metadata = [
    ('apikey', apikey),
    ('speakerids', speakerIds),
    ('encoding', encoding),
    ('samplerate', sampleRate),
    ('languagecode', languageCode)
]

from deepaffects.realtime.types import segment_chunk

responses = client.IdentifyEmotion('https://www.youtube.com/watch?v=EdHR3ZMCNBc', TIMEOUT_SECONDS, metadata=metadata)
for response in responses:
    print("Received message",response)

