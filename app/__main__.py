from aiops.logger import get_logger
from aiops.exception import AIException

import subprocess
import threading
from multiprocessing import Process
import time

logger = get_logger(__name__)

class Application:

    @classmethod
    def run_backend(cls):
        try:
            logger.info("starting backend service..")
            subprocess.run(["uvicorn" , "app.backend.api:app" , "--host" , "0.0.0.0" , "--port" , "9999"], check=True)
        except Exception as e:
            logger.error("Problem with backend service")
            raise AIException("Failed to start backend" , e)
    @classmethod
    def run_frontend(cls):
        try:
            logger.info("Starting Frontend service")
            subprocess.run(["streamlit" , "run" , "app/frontend/ui.py"],check=True)
            #,"--server.port=8501", "--server.address=0.0.0.0"
        except Exception as e:
            logger.error("Problem with frontend service")
            raise AIException("Failed to start frontend" , e)
        
if __name__=="__main__":
    try:
        threading.Thread(target=Application.run_backend).start()
        time.sleep(2)
        Application.run_frontend()
        
    except AIException as e:
        logger.error(f"CustomException occured : {str(e)}")

        