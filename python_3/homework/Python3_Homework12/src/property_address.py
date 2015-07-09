'''
Created on June 24th, 2015

@author: cbabilotte
'''
import re
import os
import logging
import configparser
from optparse import OptionParser

config_file = os.path.join(os.path.dirname(__file__), 'property_address.cfg')
config = configparser.RawConfigParser()
config.read(config_file)

LOG_FILENAME = config.get('log', 'output')
LOG_FORMAT = config.get('log', 'format')
STATE_VALIDATOR = config.get('validators', 'state')
ZIPCODE_VALIDATOR = config.get('validators', "zip_code")

DEFAULT_LOG_LEVEL = "warning"
LEVELS = {'debug'    : logging.DEBUG,
          'info'     : logging.INFO,
          'warning'  : logging.WARNING,
          'error'    : logging.ERROR,
          'critical' : logging.CRITICAL}

def start_logging(filename=LOG_FILENAME, level=DEFAULT_LOG_LEVEL):
    logging.basicConfig(filename=filename, level=LEVELS[level], format=LOG_FORMAT)
    
class Address:
    
    def __init__(self, name, street_address, city, state, zip_code):
        logging.info('Creating a new address...')
        self._name = name
        self._street_address = street_address
        self._city = city
        self._state = state 
        self._zip_code = zip_code

    @property
    def name(self):
        return self._name

    @property
    def street_address(self):
        return self._street_address

    @property
    def city(self):
        return self._city

    @property
    def state(self):
        return self._state

    @property
    def zip_code(self):
        return self._zip_code

    @street_address.setter
    def street_address(self, value):
        self._street_address = value

    @city.setter
    def city(self, value):
        self._city = value

    @state.setter
    def state(self, value):
        "State only allows 2 capital letters or it throws a StateError"
        result = re.match(STATE_VALIDATOR, value)
        if not result:
            logging.error('Not a state')
            raise StateError("Not a state")
        else:
            self._state = value

    @zip_code.setter
    def zip_code(self, value):
        "Zip code must follow the simple US pattern or it throws a ZipCodeError"
        result = re.match(ZIPCODE_VALIDATOR, value)
        if not result:
            logging.error('Invalid zip code: %s' % value)
            raise ZipCodeError("Invalid zip code")
        else:
            self._zip_code = value


class StateError(Exception):
    pass

class ZipCodeError(Exception):
    pass

if __name__ == "__main__":
    # Parse the command lines arguments
    parser = OptionParser()
    parser.add_option("-l", "--level"   , dest="level"   , action="store", help="set the log level to DEBUG, INFO, WARNING, ERROR, and CRITICAL", default="INFO")
    parser.add_option("-n", "--name"    , dest="name"    , action="store", help="set the name value of the Address")
    parser.add_option("-a", "--address" , dest="address" , action="store", help="set the street_address value of the Address")
    parser.add_option("-c", "--city"    , dest="city"    , action="store", help="set the city value of the Address")
    parser.add_option("-s", "--state"   , dest="state"   , action="store", help="set the state value of the Address")
    parser.add_option("-z", "--zip_code", dest="zip_code", action="store", help="set the zip_code value of the Address")
    (options, args) = parser.parse_args()
    
    if not options.name and not options.address and not options.city and not options.state and not options.zip_code:
        parser.error("options -n, -a, -c, -s, -z are required")
    else:
        errors = []
        if not options.name:
            errors.append("option -n requires a name for the address")
        if not options.address:
            errors.append("option -a requires a street address for the address")
        if not options.city:
            errors.append("option -c requires a city for the address")       
        if not options.state:
            errors.append("option -s requires a state for the address")
        if not options.zip_code:
            errors.append("option -z requires a zip code for the address")
        if errors:
            parser.error(errors)
            
    # Log errors
    start_logging(level=options.level)
    
    # Set property address
    try:
        home = Address(name = options.name,
                       street_address = options.address,
                       city = options.city,
                       state = options.state,
                       zip_code = options.zip_code)
    except StateError:
        parser.error("option -s requires a valid state")
    except ZipCodeError:
        parser.error("option -z requires a valud zip code")