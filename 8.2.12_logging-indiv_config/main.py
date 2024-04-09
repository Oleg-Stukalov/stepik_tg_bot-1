import logging

from module_1 import main

# Define base logging config
logging.basicConfig(format='#%(levelname)-8s %(name)s:%(funcName)s - %(message)s')

main()
