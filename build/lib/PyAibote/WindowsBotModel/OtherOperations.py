

class OtherOperations:
    """
        其他操作
        OtherOperations
    """

    def download_file(self, url: str, file_path: str, is_wait: bool) -> bool:
        """
            下载文件
            Download file

            url: 文件地址
            file_path: 文件保存的路径
            is_wait: 是否等待下载完成
            return:  总是返回True

            url: file address
            file_path: the path where the file is saved
            is_wait: Do you want to wait for the download to complete
            return: always returns True
        """
        return "true" in self.SendData("downloadFile", url, file_path, is_wait)

