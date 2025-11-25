import logging

logging.basicConfig(filename='app.log', filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s')
logging.warning('This is a warning message with a slash / in it.')

def risky_division(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        logging.error('Attempted to divide by zero: %s', e)
        return None