import sys
from openalpr import Alpr
import json

COUNTRY = 'us'
IMAGE_PATH = 'plate.jpg'

# Initialize instances
alpr = Alpr("us", "/etc/openalpr/openalpr.conf", "openalpr/runtime_data/")
if not alpr.is_loaded():
    print('Error loading Alpr')
    sys.exit(1)

# Set additional detection parameters (optional)
alpr.set_top_n(5)
alpr.set_default_region('md')

# Gather and print results
plate_results = alpr.recognize_file(IMAGE_PATH)

for i, plate in enumerate(plate_results['results']):
    print('Plate {:-<30}'.format(i))
    for c in plate['candidates']:
        display = '\t{:>7} {}'.format('{:.2f}%'.format(c['confidence']), c['plate'])
        if c['matches_template']:
            display += ' *'
        print(display)


# Call when completely done to release memory
alpr.unload()