import logging

logging.basicConfig(
    format='%(levelname)s %(name)s %(asctime)s %(filename)s %(lineno)d %(module)s %(funcName)s %(message)s', # set the format for log entries
    datefmt="%x-%X",
    filename='../LOGS/formatted.log',
    level=logging.DEBUG,
)

def main():
    function_a()
    function_b()

def function_a():
    logging.debug("danger danger")
    logging.debug("danger danger")
    logging.info("this is information")
    logging.debug("danger danger")
    logging.warning("this is a warning")
    logging.error("this is an ERROR")
    value = 38.7
    logging.error("Invalid value %s", value)

def function_b():
    logging.debug("danger danger")
    logging.info("this is information")
    logging.critical("this is critical")
    logging.debug("danger danger")
    logging.debug("danger danger")
    logging.debug("danger danger")

if __name__ == "__main__":
    main()



