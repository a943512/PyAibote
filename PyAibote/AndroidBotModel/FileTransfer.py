import re


class FileTransfer:
    """
        文件传输
        File transfer
    """
    def __push_file(self, func_name: str, to_path: str, file: bytes) -> bool:
        func_name = bytes(func_name, "utf8")
        to_path = bytes(to_path, "utf8")
        str_data = ""
        str_data += str(len(func_name)) + "/"  # func_name 字节长度
        str_data += str(len(to_path)) + "/"  # to_path 字节长度
        str_data += str(len(file)) + "\n"  # file 字节长度
        bytes_data = bytes(str_data, "utf8")
        bytes_data += func_name
        bytes_data += to_path
        bytes_data += file
        self.request.sendall(bytes_data)
        data = self.request.recv(65535)
        return data.decode("utf8")

    def __pull_file(self, *args) -> bytes:
        args_len = ""
        args_text = ""

        for argv in args:
            argv = str(argv)
            args_text += argv
            args_len += str(len(bytes(argv, 'utf8'))) + "/"
        data = (args_len.strip("/") + "\n" + args_text).encode("utf8")
        self.request.sendall(data)
        response = self.request.recv(65535)
        if response == b"":
            raise ConnectionAbortedError(f"{self.client_address[0]}:{self.client_address[1]} 客户端断开链接")
        data_length, data = response.split(b"/", 1)
        while int(data_length) > len(data):
            data += self.request.recv(65535)
        return data

    def push_file(self, origin_path: str, to_path: str) -> bool:
        """
            将电脑文件传输到手机端
            Transfer computer files to the mobile phone

            origin_path: 源文件路径
            to_path: 安卓外部存储根目录 /storage/emulated/0/
            return: True或者False

            Origin_path: source file path
            To_path: Android external storage root directory /storage/emulated/0/
            Return: True or False
        """

        if not to_path.startswith("/storage/emulated/0/"):
            to_path = "/storage/emulated/0/" + to_path

        with open(origin_path, "rb") as r:
            data = r.read()
        return "true" in self.__push_file("pushFile", to_path, data)

    def pull_file(self, remote_path: str, local_path: str) -> bool:
        """
            将手机文件传输到电脑端
            Transfer mobile phone files to the computer.

            remote_path: 手机端文件路径
            local_path: 电脑本地文件存储路径
            return: 文件字节数据

            remote_path: the file path of the mobile phone
            local_path: the local file storage path of the computer
            return: file byte data
        """
        if not remote_path.startswith("/storage/emulated/0/"):
            remote_path = "/storage/emulated/0/" + remote_path
        response = self.__pull_file("pullFile", remote_path)
        if response == b"null":
            return False
        with open(local_path, "wb") as w:
            w.write(response)
        return True