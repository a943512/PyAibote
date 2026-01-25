import re


class NewDigitalHumanOperation:
    """
        新版数字人
        New Digital human
    """

    def init_new_metahuman(self, model_folder: str, scale: int, is_paly_media_audio: bool, enable_random_param: bool, push_stream_url: bool) -> bool:
        """
            初始化数字人
            Initialize digital person

            model_folder: 模型文件夹
            scale: 缩放，1原始大小，0.5缩小一半
            is_paly_media_audio: 是否播放素材中的音频
            enable_random_param: 是否开启随机参数，随机内容：音频随机(不含数字人说话声音随机) 和 画面随机(包含平移、旋转、缩放、动作泛化)
            push_stream_url: 推流地址，默认为 "" 不推流，仅支持rtmp，例如： rtmp://your_server_ip/live/stream
            return: 成功返回True，失败返回错误信息

            model_folder: model folder
            scale: scaling, 1 original size, 0.5 reduced by half
            is_paly_media_audio: whether to play the audio in the material
            Enable_random_param: whether to turn on the random parameter, including audio random (excluding digital human voice random) 
                                 and picture random (including translation, rotation, scaling and motion generalization).
            push_stream_url: push stream address; the default value is "",and only rtmp is supported; for example, RTMP://your _ server _ IP/live/stream
            return: Returns True on success, and returns an error message on failure
        """
        return "true" in self.SendData("initNewHuman", model_folder, scale, is_paly_media_audio, enable_random_param, push_stream_url) 

    def new_get_face_data(self, server_ip: str, call_api_key: str, video_path: str) -> bool:
        """
            获取脸部数据
            Get face data

            server_ip: 服务端IP
            call_api_key: 调用密钥
            video_path: 人脸视频路径
            return:  失败返回错误信息，成功返回true。并在videoPath同级目录下生成.pt 后缀的人脸数据文件

            server_ip: server IP
            call_api_key: call key
            video_path: face video path
            return: failure returns an error message, and success returns true. And generate a face data file with. pt suffix in the same level directory of videoPath
        """
        return "true" in self.SendData("getFaceData", server_ip, call_api_key, video_path) 

    def new_metahuman_switch_action(self, figure_video_path: str, scale: int, is_paly_media_audio: bool, is_swap_color: bool, wait_play_end: bool) -> bool:
        """
            切换人物形象动作 (使用前需要先调用 init_new_metahuman 初始化数字人)
            Switch character image action

            figure_video_path: 人物视频路径
            scale: 缩放，1原始大小，0.5缩小一半
            is_paly_media_audio: 是否播放素材中的音频
            is_swap_color: 是否更换基础嘴型颜色
            wait_play_end: 等待素材播放完毕再切换，保证动作无缝衔接
            return: 成功返回True，失败返回错误信息

            figure_video_path: model folder
            scale: scaling, 1 original size, 0.5 reduced by half
            is_paly_media_audio: whether to play the audio in the material
            is_swap_color: Do you want to change the basic mouth color
            wait_play_end: Wait for the material to be played before switching to ensure the seamless connection of actions
            return: Returns True on success, and returns an error message on failure
        """
        return "true" in self.SendData("switchAction", figure_video_path, scale, is_paly_media_audio, is_swap_color, wait_play_end) 

    def new_metahuman_add_background(self, bg_path: str, x: int, y: int) -> bool:
        """
            添加视频/图片背景 (使用前需要先调用 init_new_metahuman 初始化数字人)
            Add video/picture background

            bg_path: 背景视频/图片路径
            x: 人物起始横坐标, 默认为0
            y: 人物起始纵坐标, 默认为0
            return: 成功返回True，失败返回错误信息

            bg_path: background video/picture path
            x: horizontal coordinate of character start, which is 0 by default
            y: the starting ordinate of the character, which is 0 by default
            return: Returns True on success, and returns an error message on failure
        """
        response = self.SendData("addBackground", bg_path, x, y) 
        if "true" in response:
            return True
        return response

    def new_metahuman_del_background(self) -> bool:
        """
            删除视频/图片背景
            Delete video/picture background

            return: 成功返回True，失败返回错误信息
            return: Returns True on success, and returns an error message on failure
        """
        return "true" in self.SendData("delBackground") 

    def new_metahuman_generate_human_video(self, audio_path: str) -> bool:
        """
            生成数字人视频
            Generate digital human video

            audio_path: 音频路径，需要提前生成lab文件
            return: 失败返回错误信息，成功返回true，并在audio_path同级目录下生成同名 .mp4 后缀的数字人视频文件

            audio_path: audio path. lab files need to be generated in advance.
            return: an error message is returned in case of failure, and true is returned in case of success, and a digital human video file with the same name and .mp4 suffix is generated in the same level directory of audio_path

        """
        return "true" in self.SendData("generateHumanVideo", audio_path) 

    def new_metahuman_generate_human_video_ex(self, server_ip: str, call_api_key: str, audio_path: str, video_path: str, save_video_path: str, is_music: bool = False) -> bool:
        """
            云端算力生成短视频
            Cloud computing generates short videos

            server_ip: 服务端IP
            call_api_key: 调用密钥
            audio_path: 驱动口型的音频路径
            video_path: 原视频路径
            save_video_path: 保存的合成结果路径
            is_music: 生成唱歌视频，要求 audio_path 音乐音频
            return: 失败返回错误信息，成功返回True

            server_ip: server IP
            call_api_key: call key
            audio_path: the audio path of the driving mouth
            video_path: original video path
            save_video_path: the saved composition result path
            is_music: to generate singing video, audio_path music audio is required
            return: failure returns an error message, and success returns true
        """
        return "true" in self.SendData("generateHumanVideoEx", server_ip, call_api_key, audio_path, video_path, save_video_path, is_music) 

    def new_metahuman_audio_to_lab(self, server_ip: str, audio_path: str) -> bool:
        """
            生成lab文件
            Generate lab file

            server_ip: lab服务端IP
            audio_path: 音频文件路径
            return: 失败返回错误信息，成功返回true，并在audioPath同级目录下生成同名 .lab 后缀的lab文件

            server_ip: lab server IP
            audio_path: audio file path
            return: failure returns an error message, success returns true, and a lab file with the same name. lab suffix is generated in the same directory of audioPath
        """
        return "true" in self.SendData("audioToLab", server_ip, audio_path) 

    def new_metahuman_text_to_audio(self, server_ip: str, save_audio_path: str, refer_audio_path: str, refer_text: str, text : str, speed_factor : int) -> bool:
        """
            文本转音频
            Text to audio

            server_ip: 声音克隆服务端IP
            save_audio_path: 保存的音频文件路径
            refer_audio_path: 参考音频路径
            refer_text: 参考文本内容(内容必须与参考音频播报的内容一致)
            text: 要合成的文本内容
            speed_factor: 语速，默认为1正常语速
            return: 失败返回错误信息，成功返回true

            server_ip: voice cloning server IP
            save_audio_path: the path of the saved audio file
            reference _ audio _ path: the refer_audio_path
            refer_text: Reference text content (the content must be consistent with the content broadcast by reference audio)
            text: the text content to be synthesized
            speed_factor: speech speed, which defaults to 1 normal speech speed
            return: failure returns an error message, and success returns true
        """
        return "true" in self.SendData("textToAudio", server_ip, save_audio_path, refer_audio_path, refer_text, text, speed_factor) 
    
    def new_metahuman_audio_to_text(self, server_ip: str, audio_path: str) -> bool:
        """
            语音转文本
            Speech to text

            server_ip: 语音识别服务端IP
            audio_path: 音频文件路径
            return: 失败返回"None"，成功返回语音识别的文本内容

            server_ip: IP of speech recognition server
            audio_path: audio file path
            return: "None" is returned in case of failure, and the text content of speech recognition is returned successfully
        """
        response = self.SendData("audioToText", server_ip, audio_path) 
        if response == "null":
            return None
        return response
    
    def new_metahuman_human_speak(self, audio_path: str, wait_play_sound: bool, insert_head: bool = False) -> bool:
        """
            数字人说话
            Digital people speak

            audio_path: 音频路径，需要提前生成lab文件
            wait_play_sound: 是否等待播报完毕
            insert_head: 插入队列头部,优先播报
            return: 成功返回true，失败返回错误信息

            audio_path: audio path. lab files need to be generated in advance
            wait_play_sound: Do you want to wait for the broadcast to finish
            insert_head: Insert the head of the queue and broadcast first
            return: Returns true on success, and returns an error message on failure
        """
        response = self.SendData("humanSpeak", audio_path, wait_play_sound, insert_head) 
        if "true" in response:
            return True
        return response
    
    def new_metahuman_stop_speak(self) -> bool:
        """
            打断说话
            Interrupt speech

            return: 返回true
            return: Returns true
        """
        return "true" in self.SendData("stopSpeak") 
    
    def new_metahuman_start_record(self, save_audio_path: str) -> bool:
        """
            录制麦克风
            Recording microphone

            save_audio_path: 录制保存的音频路径，需要调用 stopRecord 结束录制并保存
            return: 返回true

            save_audio_path: record the saved audio path. You need to call stopRecord to end the recording and save it
            return: returns true
        """
        return "true" in self.SendData("startRecord", save_audio_path) 
    
    def new_metahuman_stop_record(self) -> bool:
        """
            停止录制
            Stop recording

            return: 返回true
            return: returns true
        """
        return "true" in self.SendData("stopRecord") 

    def new_metahuman_train_voice_ex(self, appid: str, token: str, spk_id: str, refer_audio_path: str) -> bool:
        """
            云端算力训练声音
            Cloud computing power training voice

            appid: APP ID
            token: Access Token
            spk_id: 声音ID
            refer_audio_path: 参考音频
            return: 训练成功返回true，失败返回错误信息

            appid: APP ID
            token: Access Token
            spk_ID: sound id
            reference_audio_path: reference audio
            return: training success returns true, failure returns an error message
        """
        response = self.SendData("trainVoiceEx", appid, token, spk_id, refer_audio_path) 
        if "true" in response:
            return True
        return response
    
    def new_metahuman_get_train_status_ex(self, appid: str, token: str, spk_id: str) -> str:
        """
            获取 trainVoiceEx 训练状态
            Get the trainVoiceEx training status

            appid: APP ID
            token: Access Token
            spk_id: 声音ID
            return: 返回训练状态"Train Success"、"NotFound"、"Training"、"Failed"、unknow"   

            appid: APP ID
            token: Access Token
            spk_ID: sound id
            return: returns to the Training status of "Train Success", "NotFound", "training", "Failed" and "unknow"
        """
        response = self.SendData("getTrainStatusEx", appid, token, spk_id) 
        return response
    
    def new_metahuman_text_to_audio_ex(self, appid: str, token: str, spk_id: str, cluster: str, text: str, speed_ratio: str, save_audio_path: str, language: str = 'zh-cn') -> bool:
        """
            云端算力文本转语音
            Cloud computing power text-to-speech

            appid: APP ID
            token: Access Token
            spk_id: 声音ID
            cluster: Cluster ID  声音复刻大模型："volcano_icl"  语音合成大模型："volcano_tts"
            text: 合成的文本
            speed_ratio: 语速，正常为1
            save_audio_path: 保存的音频路径， 同时会在音频同目录下生成lab文件
            return: 成功返回true，失败返回错误信息

            appid: APP ID
            token: Access Token
            spk_ID: sound id
            cluster: Cluster ID sound reproduction model: "volcano_icl" speech synthesis model: "volcano_tts"
            text: synthesized text
            speed_ratio: speech speed, which is normally 1
            save_audio_path: the saved audio path, and a lab file will be generated in the same audio directory
            return: Returns true on success, and returns an error message on failure
        """
        response = self.SendData("textToAudioEx", appid, token, spk_id, cluster, text, speed_ratio, save_audio_path, language) 
        if "true" in response:
            return True
        return response

    def new_metahuman_get_extend_param(self) -> str:
        """
            获取驱动程序命令行参数(不包含ip和port)
            Get the driver command line parameters (excluding ip and port)

            return: 成功返回参数，失败返回None
            return: parameter is returned successfully, and None is returned on failure.
        """
        response = self.SendData("getExtendParam")
        if response == "null":
            return None
        return response
    
    def new_metahuman_get_driver_folder(self) -> str:
        """
            获取驱动程序 所在的文件夹路径
            Gets the folder path where the driver is located

            return: 返回AiDriver.exe所在的文件夹路径 
            return: Returns the folder path where AiDriver.exe is located
        """
        response = self.SendData("getDriverFolder") 
        return response

    def new_metahuman_close_driver(self) -> str:
        """
            关闭驱动
            Turn off drive

            return: 返回true
            return: Return true
        """
        response = self.SendData("closeDriver") 
        return response

    def new_metahuman_insert_video(self, video_path: str) -> bool:
        """
            插入特写视频
            Insert close-up video

            video_path: 要播放的视频
            return: 成功返回true，失败返回错误信息

            video_path: the video to play
            return: Returns true on success, and returns an error message on failure
        """
        response = self.SendData("insertVideo", video_path) 
        if "true" in response:
            return True
        return response
    
    def new_metahuman_get_human_speak_queue_count(self) -> str:
        """
            获取数字人说话 队列存入的数量
            Get the number of digital people talking queues

            return: 返回队列存入的数量
            return: Returns the amount deposited in the queue
        """
        response = self.SendData("getHumanSpeakQueueCount") 
        return response
    
    def new_metahuman_train_base_model(self, server_ip: str, call_api_key: str, video_or_image_path: str, save_folder: str) -> bool:
        """
            训练基础模型
            Training basic model

            server_ip: 服务端IP
            call_api_key: 调用密钥
            video_or_image_path: 人脸 图片/视频 路径，图片/视频 第一帧必须包含人脸且正脸对着摄像头
            save_folder: 模型保存的文件夹路径
            return: 失败返回错误信息，成功返回True。模型保存在 saveFolder 文件夹下。一般耗时60分钟左右

            server_ip: server IP
            call_api_key: call key
            video_or_image_path: the path of face picture/video. The first frame of picture/video must contain face and face the camera
            save_folder: the folder path where the model is saved
            return: failure returns an error message, and success returns true
                    he model is saved in the saveFolder folder. It usually takes about 60 minutes
        """
        response = self.SendData("trainBaseModel", server_ip, call_api_key, video_or_image_path, save_folder) 
        if "true" in response:
            return True
        return response
    
    def new_metahuman_audio_to_lab_ex(self, access_key_id: str, access_key_secret: str, app_key: str, audio_path: str) -> str:
        """
            云端生成lab文件(对接阿里云语音识别极速版)
            Cloud Generation lab File (Docking Alibaba Cloud Speech Recognition Extreme Edition)

            access_key_id: 密钥ID
            access_key_secret: 密钥
            app_key: app密钥
            audio_path: 音频文件路径
            return: 失败返回错误信息，成功返回True，并在audioPath同级目录下生成同名 .lab 后缀的lab文件  

            access_key_ID: key id
            access_key_secret: key
            app_key: app key
            audio_path: audio file path
            return: failure returns an error message, success returns true, and a lab file with the same name. 
                    lab suffix is generated in the same directory of audioPath
        """
        response = self.SendData("audioToLabEx", access_key_id, access_key_secret, app_key, audio_path) 
        if "true" in response:
            return True
        return response
    
    def new_metahuman_hide_human_window(self, is_hide) -> bool:
        """
            隐藏数字人窗口
            Hidden numbers ren Chuang kou

            is_hide: 是否隐藏, True 隐藏, False 显示
            return: 返回True

            is_hide: whether to hide, True to hide, false to display
            return: Returns True
        """
        return "true" in self.SendData("hideHumanWindow", is_hide) 
    
    def new_metahuman_del_human_window_border(self, is_no_border) -> bool:
        """
            删除数字人窗口标题栏边框
            Delete the title bar border of the Digital Man window

            is_no_border: 是否删除标题栏边框, True 删除标题栏, False 恢复
            return: 返回True

            is_no_border: whether to delete the title bar border, true to delete the title bar, false to restore
            return: returns true
        """
        return "true" in self.SendData("delHumanWindowBorder", is_no_border) 
    
    def new_metahuman_llm(self, app_id: str, api_key: str, prompt: str) -> str:
        """
            通义千问(应用)
            General meaning and thousand questions (application)

            app_id: 应用ID
            api_key: API密钥
            prompt: 提问
            return: 成功输出语言模型答案，失败返回错误信息 

            app_id: application ID
            api_key: API key
            prompt: ask questions
            return: the language model answer is successfully output, 
                     and an error message is returned if it fails
        """
        response = self.SendData("llm", app_id, api_key, prompt) 
        return response
    
    def new_metahuman_get_face_data_service(self, video_path: str) -> str:
        """
            获取脸部数据(中转服务)
            Get face data (transit service)

            video_path: 人脸视频路径
            return: 失败返回错误信息，成功返回True。并在videoPath同级目录下生成.pt 后缀的人脸数据文件 

            video_path: face video path.
            return: failure returns an error message, and success returns true. 
                    And generate a face data file with. pt suffix in the same level directory of videoPath.
        """
        response = self.SendData("getFaceData_Service", video_path) 
        if "true" in response:
            return True
        return response

    def new_metahuman_train_base_model_service(self, video_or_image_path: str, save_folder: str) -> str:
        """
            训练基础模型(中转服务)
            Training basic model (transit service)

            video_or_image_path: 人脸 图片/视频 路径，图片/视频 第一帧必须包含人脸且正脸对着摄像头
            save_folder: 模型保存的文件夹路径
            return: 失败返回错误信息，成功返回True。模型保存在 saveFolder 文件夹下。一般耗时60分钟左右

            video_or_image_path: the path of face picture/video. The first frame of picture/video must contain face and face the camera.
            save_folder: the folder path where the model is saved.
            return: failure returns an error message, and success returns true. 
                    The model is saved in the saveFolder folder. It usually takes about 60 minutes.
        """
        response = self.SendData("trainBaseModel_Service", video_or_image_path, save_folder) 
        if "true" in response:
            return True
        return response
    
    def new_metahuman_generate_human_video_ex_service(self, audio_path: str, video_path: str, save_video_path: str, is_music: bool = False) -> str:
        """
            云端算力生成短视频(中转服务)
            Cloud computing generates short video (transit service)

            audio_path: 驱动口型的音频路径
            video_path: 原视频路径
            save_video_path: 保存的合成结果路径
            is_music: 生成唱歌视频，要求 audio_path 音乐音频
            return: 失败返回错误信息，成功返回True

            audio_path: the audio path of the driving mouth.
            video_path: original video path.
            save_video_path: the saved composition result path.
            is_music: to generate singing video, audio_path music audio is required.
            return: failure returns an error message, and success returns true.
        """
        response = self.SendData("generateHumanVideoEx_Service", audio_path, video_path, save_video_path, is_music) 
        if "true" in response:
            return True
        return response
    
    def new_metahuman_train_voice_ex_service(self, refer_audio_path: str) -> str:
        """
            云端算力训练声音(火山引擎)(中转服务)
            Cloud Computing Training Voice (Volcano Engine) (Transit Service)

            refer_audio_path: 参考音频
            return: 训练成功返回True，失败返回错误信息

            refer_audio_path: reference audio.
            return: training success returns true, failure returns an error message.
        """
        response = self.SendData("trainVoiceEx_Service", refer_audio_path) 
        if "true" in response:
            return True
        return response

    def new_metahuman_text_to_audio_ex_service(self, spk_id: str, cluster: str, text: str, speed_ratio: str, save_audio_path: str, language: str = 'zh-cn') -> str:
        """
            云端算力文本转语音(火山引擎)(中转服务)
            Cloud Computing Text-to-Speech (Volcano Engine) (Transit Service)

            spk_id: 声音复刻大模型的声音ID 语音合成大模型的Voice_type
            cluster: Cluster ID  声音复刻大模型："volcano_icl"     语音合成大模型："volcano_tts"
            text: 合成的文本
            speed_ratio: 语速，正常为1
            save_audio_path: 保存的音频路径， 同时会在音频同目录下生成lab文件
            language: 语言，中文（zh-cn）、英语（en）、西班牙语（es）、法语（fr）、德语（de）、俄语（ru）、日语（ja）、阿拉伯语（ar）、印地语（hi）、葡萄牙语（pt）
            return: 失败返回错误信息，成功返回True

            spk_ID: the voice id of the voice reproduction model and the Voice_type of the speech synthesis model.
            cluster: Cluster ID sound reproduction model: "volcano_icl" speech synthesis model: "volcano_tts"
            text: synthesized text
            speed_ratio: speech speed, which is normally 1.
            save_audio_path: the saved audio path, and a lab file will be generated in the same audio directory.
            language: languages: Chinese (zh-cn), English (en), Spanish (es), 
                     French (fr), German (de), Russian (ru), Japanese (ja), Arabic (ar), hindi (Hi) and Portuguese (pt).
            return: failure returns an error message, and success returns true.
        """
        response = self.SendData("textToAudioEx_Service", spk_id, cluster, text, speed_ratio, save_audio_path, language) 
        if "true" in response:
            return True
        return response

    def new_metahuman_audio_to_lab_ex_service(self, audio_path: str) -> str:
        """
            云端生成lab文件(对接阿里云语音识别极速版)(中转服务)
            Cloud-generated lab file (connected to Alibaba Cloud Speech Recognition Extreme Edition) (transit service)

            audio_path: 音频文件路径
            return: 失败返回错误信息，成功返回True，并在audioPath同级目录下生成同名 .lab 后缀的lab文件

            audio_path: audio file path.
            return: failure returns an error message, success returns true, and a lab file with the same name. 
                    lab suffix is generated in the same directory of audioPath.
        """
        response = self.SendData("audioToLabEx_Service", audio_path) 
        if "true" in response:
            return True
        return response

    def new_metahuman_llm_service(self, prompt: str) -> str:
        """
            通义千问(应用)(中转服务)
            Tong yi Qian Wen (application) (transit service)

            prompt: 提问
            return: 成功输出语言模型答案，失败返回错误信息

            prompt: ask questions
            return: successfully output the language model answer, and return an error message if it fails.
        """
        response = self.SendData("llm_Service", prompt) 
        return response
    
    def new_metahuman_get_windows_id(self) -> str:
        """
            获取 windows ID
            get windows ID

            return: 成功返回windows Id
            return: successfully returned windows Id
        """
        response = self.SendData("getWindowsId") 
        return response
    
    def new_metahuman_blur_mouth(self, is_blur_mouth: str) -> str:
        """
            高斯模糊嘴型，优化嘴型细节瑕疵
            Gaussian fuzzy mouth shape, optimizing mouth shape detail defects

            isBlurMouth: 开启后淡化口型瑕疵细节，嘴型清晰度会降低
            return: 成功返回true

            isBlurMouth: After opening, the details of the mouth defects will be diluted, 
                        and the mouth definition will be reduced
            return: returned true successfully
        """
        return "true" in self.SendData("blurMouth", is_blur_mouth) 