#logging means--Capture details, which are useful while
# debugging and show user details about execution of the program

#Showing worning to the users
#show information to the users
#show critical Error, Critical error to the user

import logging

def test_print_logs():
    LOGGER = logging.getLogger(__name__) #__name__ is automatically takes as file name in this case

    #intentional Logging to Users
    LOGGER.info("this is Infomation Logs")
    LOGGER.warning("This is Warning Logs")
    LOGGER.critical("This is Error Logs")
    LOGGER.error("This is an error Logs")
