import traceback

class SendClientData:
    """
        将TCP数据发送给驱动程序
        Give TCP data to the driver
    """

    def SendData(self, *args) -> str:
        args_len = ""
        args_text = ""
        
        for argv in args:
            if argv is None:
                argv = ""
            elif isinstance(argv, bool) and argv:
                argv = "true"
            elif isinstance(argv, bool) and not argv:
                argv = "false"
            argv = str(argv)
            args_text += argv
            args_len += str(len(bytes(argv, 'utf8'))) + "/"
        data = (args_len.strip("/") + "\n" + args_text).encode("utf8")
        try:
            response = self.StarLoadWait(data)
            return response
        except Exception as e:
            self.error("send/read tcp data error: " + str(traceback.format_exc()))
            raise e