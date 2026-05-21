from .BaseController import BaseController
from fastapi import UploadFile

class DataController(BaseController):

    def __init__(self):
        super().__init__()


    def validate_uploaded_file(self,file : UploadFile):

        SIZE_DIVISOR = 1024 * 1024  # 1MB in bytes

        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return {
                "status" : "error",
                "message" : "Invalid file type"
            }

        if file.size > self.app_settings.FILE_MAX_SIZE * SIZE_DIVISOR:
            return {
                "status" : "error",
                "message" : "File size exceeds the limit"
            }    

        return {
            "status" : "success",
            "message" : "File is valid"
        }