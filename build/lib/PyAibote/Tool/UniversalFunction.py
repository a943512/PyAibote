import base64
from PIL import Image
from io import BytesIO
import psutil

class UniversalFunction:

    def SaveBase64Png(self, Base64Data, OutputPath):
        try:
            imgData = base64.b64decode(Base64Data)
            with open(OutputPath, "wb") as f:
                f.write(imgData)
        except Exception as e:
            print(f"Failed to report the wrong picture. Please save it yourself ErrorMsg: {e}")

    def check_process(self, process_name):
        for proc in psutil.process_iter(['pid', 'name']):
            if process_name == proc.info['name']:
                return True
        return False
    





