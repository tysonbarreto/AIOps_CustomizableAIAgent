import os, sys
from pathlib import Path
import logging
from datetime import datetime


def get_logger(name):
    filename=os.path.join("logs",f"log_{datetime.now().strftime("%Y-%m-%d")}.log")
    os.makedirs(name=os.path.dirname(filename), exist_ok=True)

    logging.basicConfig(
        filename=filename,
        format="[%(asctime)s] - %(filename)s - %(levelname)s : %(message)s",
        level=logging.INFO
)
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger

if __name__=="__main__":
    __all__ = ["get_logger"]
