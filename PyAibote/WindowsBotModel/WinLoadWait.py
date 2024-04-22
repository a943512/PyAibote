import time
import copy


class WinLoadWait:
    """
        隐式等待和显示等待
        Implicit waiting and explicit waiting
    """

    Implicit_Waiting = 0
    Implicit_Waiting_Frequency = 0
    Implicit_Waiting_Throwing = False
    Show_Waiting = 0
    Show_Waiting_Frequency = 0
    Show_Waiting_Throwing = False

    def _Send(self,data):
        self.debug(rf"->>> {data}")

        self.request.sendall(data)
        response = self.request.recv(87654)
        if response == b"":
            raise ConnectionAbortedError(f"{self.client_address[0]}:{self.client_address[1]} Client disconnects")
        data_length, data = response.split(b"/", 1)
        while int(data_length) > len(data):
            data += self.request.recv(87654)

        response = data.decode('UTF-8')
        if len(response) > 10000:
            self.debug(rf"<-<- {response[:100]}......")
        else:
            self.debug(rf"<-<- {response}")
        if response == b"":
            raise ConnectionAbortedError(f"{self.client_address[0]}:{self.client_address[1]} Client disconnects")
        
        return response

    def StarLoadWait(self, data):
        response = self._Send(data)
        return response

    def StartShowWait(self, Time: int, RotationTime: int, ThrowException: bool):
        """
            进行隐式等待和显示等待模式的切换
            Switch between implicit waiting and display waiting modes.
        """
        self.debug(rf"---- Enter the display waiting mode waiting time：{Time}s")
        self.Show_Waiting = copy.deepcopy(self.Implicit_Waiting)
        self.Show_Waiting_Frequency = copy.deepcopy(self.Implicit_Waiting_Frequency)
        self.Show_Waiting_Throwing = copy.deepcopy(self.Implicit_Waiting_Throwing)

        self.Implicit_Waiting = Time
        self.Implicit_Waiting_Frequency = RotationTime
        self.Implicit_Waiting_Throwing = ThrowException

    def EndShowWait(self):
        """
            进行隐式等待和显示等待模式的切换
            Switch between implicit waiting and display waiting modes.
        """
        self.debug(rf"---- Finish the display waiting mode")
        self.Implicit_Waiting = self.Show_Waiting
        self.Implicit_Waiting_Frequency = self.Show_Waiting_Frequency
        self.Implicit_Waiting_Throwing = self.Show_Waiting_Throwing