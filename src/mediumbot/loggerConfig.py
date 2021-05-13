import logging

# from logging.config import fileConfig


class loggerConfig:
    
    logging_level = "INFO"
    logging_datefmt = "%m/%d/%Y %H:%M:%S"
    logging_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging_file = "logger.log"

    def __init__(self, file, *args, **kwargs):
        pass

    def startLogger(self):
        
        logging.basicConfig(
                level=getattr(logging, self.logging_level),
                format=self.logging_format,
                datefmt=self.logging_datefmt,
                filename=self.logging_file,
                filemode='w')

        # create console handler and set level to debug
        ch = logging.StreamHandler()
        ch.setLevel(getattr(logging, self.logging_level))
        
        # create formatter
        formatter = logging.Formatter(self.logging_format)
        
        # add formatter to ch
        ch.setFormatter(formatter)

        # add ch to logger
        logging.getLogger().addHandler(ch)

        self.logger = logging.getLogger()


    def loggerConfig(self, file):
        logging.fileConfig(file)
        self.logger = logging.getLogger()
