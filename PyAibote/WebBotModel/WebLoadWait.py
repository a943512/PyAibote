import time
import copy


class WebLoadWait:
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
        response = self.request.recv(65535)
        response = response.decode('UTF-8')
        if len(response) > 10000:
            self.debug(rf"<-<- {response[:100]}......")
        else:
            self.debug(rf"<-<- {response}")
        if response == b"":
            raise ConnectionAbortedError(f"{self.client_address[0]}:{self.client_address[1]} Client disconnects")
        return response

    def StarLoadWait(self, data):
        response = self._Send(data)
        start_time = time.time()
        if 'false' in response or 'webdriver error' in response:
            while time.time() - start_time < self.Implicit_Waiting:
                try:
                    self.debug(rf"---- Cannot find element. Retrying....  No retry in {self.Implicit_Waiting}s   {round(time.time() - start_time, 2)}s")
                    response = self._Send(data)
                    if 'false' not in response and 'webdriver error' not in response:
                        break
                    if "domain" in response or "path" in response or "secure" in response or "httpOnly" in response:
                        break
                    time.sleep(self.Implicit_Waiting_Frequency)
                except Exception as e:
                    time.sleep(self.Implicit_Waiting_Frequency)
            if self.Implicit_Waiting_Throwing:
                if 'false' in response or 'webdriver error' in response:
                    raise "Unable to find the specified element"
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