import re


class DigitalHumanOperation:
    """
        数字人
        Digital human
    """

    def init_metahuman(self, metahuman_mde_path: str, metahuman_scale_width: int, metahuman_scale_height: int, is_update_metahuman: bool = False) -> bool:
        """
            初始化数字人，第一次初始化需要一些时间
            Initializing digital people, it takes some time to initialize for the first time.

            metahuman_mde_path: 数字人模型路径
            metahuman_scale_width: 数字人宽度缩放倍数，1为原始大小。为2时放大一倍，0.5则缩小一半
            metahuman_scale_height: 数字人高度缩放倍数，1为原始大小。为2时放大一倍，0.5则缩小一半
            is_update_metahuman: 是否强制更新，默认fasle。为true时强制更新会拖慢初始化速度
            return: True或者False

            metahuman_mde_path: Digital human model path
            metahuman_scale_value: Digital people zoom multiple, 1 is the original size. When it is 0.5, it is doubled, and when it is 2, it is halved
            is_update_metahuman: Whether to force update, fasle by default. When true, forcing the update will slow down the initialization speed
            return: True or False
        """
        return "true" in self.SendData("initMetahuman", metahuman_mde_path, metahuman_scale_width, metahuman_scale_height, is_update_metahuman) 

    def metahuman_speech(self, save_voice_folder: str, text: str, language: str, voice_name: str, quality: int = 0, wait_play_sound: bool = True, speech_rate: int = 0, voice_style: str = "General") -> bool:
        """
            数字人说话，此函数需要调用 initSpeechService 初始化语音服务
            Digital people speak, this function needs to call initSpeechService to initialize voice service

            save_voice_folder: 保存的发音文件目录，文件名以0开始依次增加，扩展为.mp3格式
            text: 要转换语音的文本
            language: 语言，参考开发文档 语言和发音人
            voice_name: 发音人，参考开发文档 语言和发音人
            quality: 音质，0低品质  1中品质  2高品质， 默认为0低品质
            wait_play_sound: 等待音频播报完毕，默认为 true等待
            speech_rate:  语速，默认为0，取值范围 -100 至 200
            voice_style: 语音风格，默认General常规风格，其他风格参考开发文档 语言和发音人
            return: True或者False

            save_voice_folder: the directory of saved pronunciation files. The file names are increased from 0 and expanded to. wav format
            text: the text to be converted into speech
            language: language, reference development document language and speaker
            Voice_name: speaker, refer to the development document language and speaker
            quality: sound quality, 0 low quality 1 medium quality 2 high quality, and 0 low quality by default
            wait_play_sound: Wait until the audio broadcast is finished; the default value is true
            speech_rate: speech speed, which is 0 by default, and the value range is -100 to 200
            voice_style: voice style, the default General style, and other styles refer to the development document language and speaker
            return: True or False
        """
        return  "false" not in self.SendData("metahumanSpeech", save_voice_folder, text, language, voice_name, quality,wait_play_sound, speech_rate, voice_style) 

    def metahuman_speech_cache(self, save_voice_folder: str, text: str, language: str, voice_name: str, quality: int = 0, wait_play_sound: bool = True, speech_rate: int = 0, voice_style: str = "General") -> bool:
        """
            *数字人说话缓存模式，需要调用 initSpeechService 初始化语音服务。函数一般用于常用的话术播报，非常用话术切勿使用，否则内存泄漏
            * Digital people speak in cache mode, which requires calling initSpeechService to initialize voice service. Function is generally used for common speech broadcasting, and it should not be used if it is very popular, otherwise the memory will leak
            
            save_voice_folder: 保存的发音文件目录，文件名以0开始依次增加，扩展为.wav格式
            text: 要转换语音的文本
            language: 语言，参考开发文档 语言和发音人
            voice_name: 发音人，参考开发文档 语言和发音人
            quality: 音质，0低品质  1中品质  2高品质， 默认为0低品质
            wait_play_sound: 等待音频播报完毕，默认为 true等待
            speech_rate:  语速，默认为0，取值范围 -100 至 200
            voice_style: 语音风格，默认General常规风格，其他风格参考开发文档 语言和发音人
            return: True或者False

            save_voice_folder: the directory of saved pronunciation files. The file names are increased from 0 and expanded to. wav format
            text: the text to be converted into speech
            language: language, reference development document language and speaker
            voice_name: speaker, refer to the development document language and speaker
            quality: sound quality, 0 low quality 1 medium quality 2 high quality, and 0 low quality by default
            wait_play_sound: Wait until the audio broadcast is finished; the default value is true
            speech_rate: speech speed, which is 0 by default, and the value range is -100 to 200
            voice_style: voice style, the default General style, and other styles refer to the development document language and speaker
            return: True or False
        """
        return "true" in self.SendData("metahumanSpeechCache", save_voice_folder, text, language, voice_name, quality, wait_play_sound, speech_rate, voice_style)

    def metahuman_insert_video(self, video_file_path: str, audio_file_path: str, wait_play_video: bool = True) -> bool:
        """
            数字人插入视频
            Digital people insert videos.

            video_file_path: 插入的视频文件路径
            audio_file_path: 插入的音频文件路径
            wait_play_video: 等待视频播放完毕，默认为 true等待
            return: True或者False

            video_file_path: the path of the inserted video file
            audio_file_path: the path of the inserted audio file
            wait_play_video: Wait until the video is finished; the default value is true
            return: True or False
        """
        return "true" in self.SendData("metahumanInsertVideo", video_file_path, audio_file_path, wait_play_video) 

    def replace_background(self, bg_file_path: str, replace_red: int = -1, replace_green: int = -1, replace_blue: int = -1, sim_value: int = 0) -> bool:
        """
            替换数字人背景
            Replace the background of digital people

            bg_file_path: 数字人背景 图片/视频 路径，默认不替换背景。仅替换绿幕背景的数字人模型
            replace_red: 数字人背景的三通道之一的 R通道色值。默认-1 自动提取
            replace_green: 数字人背景的三通道之一的 G通道色值。默认-1 自动提取
            replace_blue: 数字人背景的三通道之一的 B通道色值。默认-1 自动提取
            sim_value: 相似度。 默认为0，取值应当大于等于0
            return: True或者False

            bg_file_path: the background picture/video path of digital people, which does not replace the background by default. Digital human model only replacing green screen background
            replace_red: R channel color value of one of the three channels of digital human background. Default -1 automatic extraction
            replace_green: the G-channel color value of one of the three channels of digital human background. Default -1 automatic extraction
            replace_blue: B-channel color value of one of the three channels of digital human background. Default -1 automatic extraction
            sim_value: similarity. The default value is 0 and the value should be greater than or equal to 0
            return: True or False
        """
        return "true" in self.SendData("replaceBackground", bg_file_path, replace_red, replace_green, replace_blue, sim_value) 

    def show_speech_text(self, origin_y: int = 0, font_type: str = "Arial", font_size: int = 30, font_red: int = 128,font_green: int = 255, font_blue: int = 0, italic: bool = False,underline: bool = False) -> bool:
        """
            显示数字人说话的文本
            Displays the text spoken by a digital person

            origin_y, 第一个字显示的起始Y坐标点。 默认0 自适应高度
            font_type, 字体样式，支持操作系统已安装的字体。例如"Arial"、"微软雅黑"、"楷体"
            font_size, 字体的大小。默认30
            font_red, 字体颜色三通道之一的 R通道色值。默认128
            font_green, 字体颜色三通道之一的 G通道色值。默认255
            font_blue, 字体颜色三通道之一的 B通道色值。默认0
            italic, 是否斜体,默认false
            underline, 是否有下划线,默认false
            return: True或者False

            origin_y, the starting y coordinate point displayed by the first word. Default 0 Adaptive Height
            font_type, font style, supports fonts installed in the operating system. For example, "Arial", "Microsoft yahei" and "italics"
            font_size, the size of the font. Default 30
            font_red, the R channel color value of one of the three channels of font color. Default 128
            font_green, the color value of G channel, one of the three channels of font color. Default 255
            font_blue, the color value of B channel, which is one of the three channels of font color. Default 0
            italic, italic or not, the default is false
            underline, whether it is underlined or not, the default is false
            return: True or False
        """
        return "true" in self.SendData("showSpeechText", origin_y, font_type, font_size, font_red, font_green, font_blue,italic, underline) 

    def make_metahuman_video(self, save_video_folder: str, text: str, language: str, voice_name: str, bg_file_path: str, sim_value: float = 0, voice_style: str = "General", quality: int = 0, speech_rate: int = 0,) -> bool:
        """
            生成数字人短视频，此函数需要调用 initSpeechService 初始化语音服务
            To generate short video of digital people, this function needs to call initSpeechService to initialize voice service

            save_video_folder: 保存的视频目录
            text: 要转换语音的文本
            language: 语言，参考开发文档 语言和发音人
            voice_name: 发音人，参考开发文档 语言和发音人
            bg_file_path: 数字人背景 图片/视频 路径，扣除绿幕会自动获取绿幕的RGB值，null 则不替换背景。仅替换绿幕背景的数字人模型
            sim_value: 相似度，默认为0。此处参数用作绿幕扣除微调RBG值。取值应当大于等于0
            voice_style: 语音风格，默认General常规风格，其他风格参考开发文档 语言和发音人
            quality: 音质，0低品质  1中品质  2高品质， 默认为0低品质
            speech_rate:  语速，默认为0，取值范围 -100 至 200
            return: True或者False

            save_video_folder: the saved video directory
            text: the text to be converted into speech
            language: language, reference development document language and speaker
            voice_name: speaker, refer to the development document language and speaker
            bg_file_path: the background picture/video path of the digital person. If the green screen is subtracted, the RGB value of the green screen will be automatically obtained; if it is null, the background will not be replaced. Digital human model only replacing green screen background
            sim_value: similarity, which defaults to 0. Here, the parameter is used as the RBG value of green screen subtraction fine tuning. Value should be greater than or equal to 0
            voice_style: voice style, the default General style, and other styles refer to the development document language and speaker
            quality: sound quality, 0 low quality 1 medium quality 2 high quality, and 0 low quality by default
            speech_rate: speech speed, which is 0 by default, and the value range is -100 to 200
            return: True or False
        """
        return "true" in self.SendData("makeMetahumanVideo", save_video_folder, text, language, voice_name, bg_file_path, sim_value, voice_style, quality, speech_rate) 

    def init_speech_clone_service(self, api_key: str, voice_id: str) -> bool:
        """
            初始化数字人声音克隆服务(不支持win 7系统)  声音克隆服务卡密获取网站：elevenlabs.io
            Initialize the digital human voice cloning service (win 7 system is not supported). The voice cloning service card is obtained from the website: elevenlabs.io

            api_key: API密钥
            voice_id: 声音ID
            return: True或者False

            api_key: API key
            clone_val: Voice ID
            return: True or False
        """
        return "true" in self.SendData("initSpeechCloneService", api_key, voice_id) 

    def metahuman_speech_clone(self, save_audio_path: str, text: str, language: str = "zh-cn", wait_play_sound: bool = True) -> bool:
        """
            数字人使用克隆声音说话，此函数需要调用 initSpeechCloneService 初始化语音服务
            Generate digital human speech file (voice clone), and automatically generate MP3 file and lab file

            save_audio_path: 保存的发音文件路径, 这里是文件路径，不是目录！
            text: 要转换语音的文本
            language: 语言，中文：zh-cn，其他语言：other-languages
            wait_play_sound: 等待音频播报完毕，默认为 true等待
            return: True或者False

            save_audio_path: the path of the saved pronunciation file, here is the file path, not the directory!
            text: the text to be converted into speech
            language: language, Chinese: zh-cn, other languages: other-languages
            wait_play_sound: Wait until the audio broadcast is finished; the default value is true
            return: True or False
        """
        return "true" in self.SendData("metahumanSpeechClone", save_audio_path, text, language, wait_play_sound) 

    def make_metahuman_video_clone(self, save_video_folder: str, text: str, language: str = "zh-cn", bg_file_path: str = "", sim_value: int = 0) -> bool:
        """
            使用克隆声音生成数字人短视频，此函数需要调用 initSpeechCloneService 初始化语音服务
            Using cloned voice to generate short video of digital people, this function needs to call initSpeechCloneService to initialize voice service

            save_video_folder: 保存的视频和音频文件目录
            text: 要转换语音的文本
            language: 语言，语言，中文：zh-cn，其他语言：other-languages
            bg_file_path: 数字人背景 图片/视频 路径，扣除绿幕会自动获取绿幕的RGB值，null 则不替换背景。仅替换绿幕背景的数字人模型
            sim_value: 相似度，默认为0。此处参数用作绿幕扣除微调RBG值。取值应当大于等于0
            return: True或者False

            save_video_folder: directory of saved video and audio files
            text: the text to be converted into speech
            language: language, language, Chinese: zh-cn, other languages: other-languages
            bg_file_path: the background picture/video path of the digital person. If the green screen is subtracted, the RGB value of the green screen will be automatically obtained; if it is null,
                          the background will not be replaced. Digital human model only replacing green screen background
            sim_value: similarity, which defaults to 0. Here, the parameter is used as the RBG value of green screen subtraction fine tuning. Value should be greater than or equal to 0
            return: True or False
        """
        return "true" in self.SendData("makeMetahumanVideoClone", save_video_folder, text, language, bg_file_path, sim_value) 


    def make_metahuman_speech_file_clone(self, save_audio_path: str, text: str, language: str = "zh-cn") -> bool:
        """
            生成数字人说话文件(声音克隆)，生成MP3文件和 lab文件，提供给 metahumanSpeechByFile 和使用
            Generate digital human speech file (voice clone), MP3 file and lab file, and provide them to metahumanSpeechByFile and use it

            save_audio_path: 保存的发音文件路径。这里是路径，不是目录！
            text: 要转换语音的文本
            language: 语言，中文：zh-cn，其他语言：other-languages
            return: True或者False

            save_audio_path: the path of the saved pronunciation file. This is a path, not a directory!
            text: the text to be converted into speech
            language: language, Chinese: zh-cn, other languages: other-languages
            return: True or False
        """
        return "true" in self.SendData("makeMetahumanSpeechFileClone", save_audio_path, text, language) 

    def metahuman_speech_byFile(self, audio_path: str, wait_play_sound : bool = True) -> bool:
        """
            数字人说话文件缓存模式
            Cache mode of digital human speech file

            audio_path: 音频路径， 同名的 .lab文件需要和音频文件在同一目录下
            wait_play_sound: 是否等待播报完毕，默认为true 等待
            return: True或者False

            audio_path: Audio path. lab file with the same name needs to be in the same directory as the audio file
            wait_play_sound: whether to wait for the broadcast, the default value is true
            return: True or False
        """
        return "true" in self.SendData("metahumanSpeechByFile", audio_path, wait_play_sound) 

    def metahuman_speech_break(self) -> bool:
        """
            打断数字人说话，一般用作人机对话场景。metahumanSpeech和metahumanSpeechCache的 waitPlaySound 参数 设置为false时，此函数才有意义
            Interrupting a digital person's speech is generally used as a human-computer conversation scene. 
            This function only makes sense when the waitPlaySound parameter of metahumanSpeech and metahumanSpeechCache is set to false

            return: 返回true打断正在说话， 返回false 则为未说话状态
            return true to interrupt talking, return false to be silent
        """
        return "true" in self.SendData("metahumanSpeechBreak") 

    def make_metahuman_speech_file(self, save_audio_path: str, text: str, language: str = "zh-cn", voice_name: str = "", quality: int = 0, speech_rate: int = 0, voice_style: str = "General") -> bool:
        """
            生成数字人说话文件，生成MP3文件和 lab文件，提供给 metahumanSpeechByFile 和使用
            Generate digital human speech files, MP3 files and lab files, and provide them to metahumanSpeechByFile and use

            save_audio_path: 保存的音频文件路径，扩展为.MP3格式。同名的 .lab文件需要和音频文件在同一目录下
            text: 要转换语音的文本
            language: 语言，参考开发文档 语言和发音人
            voice_name: 发音人，参考开发文档 语言和发音人
            quality: 音质，0低品质  1中品质  2高品质， 默认为0低品质
            speech_rate: 语速，默认为0，取值范围 -100 至 200
            voice_style: 语音风格，默认General常规风格，其他风格参考开发文档 语言和发音人
            return: True或者False

            save_audio_path: the path of the saved audio file, expanded to .mp3 format. The. lab file with the same name needs to be in the same directory as the audio file
            text: the text to be converted into speech
            language: language, reference development document language and speaker
            voice_name: speaker, refer to the development document language and speaker
            quality: sound quality, 0 low quality 1 medium quality 2 high quality, and 0 low quality by default
            speech_rate: speech speed, which is 0 by default, and the value range is -100 to 200
            voice_style: voice style, the default General style, and other styles refer to the development document language and speaker
            return: True or False
        """
        return "true" in self.SendData("makeMetahumanSpeechFile", save_audio_path, text, language, voice_name, quality, speech_rate, voice_style) 

    def switch_action(self, call_apiKey: str, action_video_or_image: str, user_simValue: bool) -> bool:
        """
            切换新的人物形象动作，此函数无需训练数字人模型，直接切换各种人物形象动作和场景
            Switch new character movements. This function can directly switch various character movements and scenes without training digital human models

            call_apiKey: 调用函数的密钥
            action_video_or_image: 闭嘴的人物视频或者图片
            user_simValue: 是否使用近似值加速(影响精度)，默认不加速
            return: True或者False

            call_apiKey: String, the key of the calling function
            action_video_or_image: a string, shut-up character video or picture
            return: True or False
        """
        return "true" in self.SendData("switchAction", call_apiKey, action_video_or_image, user_simValue) 

    def train_human_model(self, call_apiKey: str, train_video_or_image: str, src_metahuman_model_path: str, save_human_model_folder: str) -> bool:
        """
            训练数字人，训练时长为10-30分钟
            Train digital people for 10-30 minutes

            call_apiKey: 调用函数的密钥
            train_video_or_image: 闭嘴的人物视频或者图片 素材
            src_metahuman_model_path: 预训练数字人模型路径
            save_human_model_folder: 保存训练完成的模型目录
            return: True或者False

            call_apiKey: the key of the calling function
            train_video_or_image: shut up the character video or picture material
            src_metahuman_model_path: the path of pre-training digital human model
            save_human_model_folder: save the model directory after training
            return: True or False
        """
        return "true" in self.SendData("trainHumanModel", call_apiKey, train_video_or_image, src_metahuman_model_path, save_human_model_folder) 

    def make_metahuman_video_by_file(self, audio_path: str, bg_file_path: str, sim_value: str = 0) -> bool:
        """
            通过音频文件生成数字人短视频， 此函数依赖 initMetahuman 函数运行，否则程序会崩溃
            Switch new character movements. This function can directly switch various character movements and scenes without training digital human models

            audio_path: 字符串型，音频路径， 同名的 .lab文件需要和音频文件在同一目录下
            bg_file_path: 字符串型，数字人背景 图片/视频 路径，扣除绿幕会自动获取绿幕的RGB值，null 则不替换背景。仅替换绿幕背景的数字人模型
            sim_value: 整型，相似度，默认为0。此处参数用作绿幕扣除微调RBG值。取值应当大于等于0
            return: True or False

            audio_path: String type, audio path, and. lab file with the same name need to be in the same directory as the audio file
            bg_file_path: String type, background picture/video path of digital person. If the green screen is subtracted, the RGB value of the green screen will be automatically obtained,
                           and null will not replace the background. Digital human model only replacing green screen background
            sim_value: Integer, similarity, default is 0. Here, the parameter is used as the RBG value of green screen subtraction fine tuning
                       Value should be greater than or equal to 0
            return: True or False
        """
        return "true" in self.SendData("makeMetahumanVideoByFile", audio_path, bg_file_path, sim_value) 

    def get_switch_action_state(self) -> bool:
        """
            获取切换人物形象动作状态
            Obtain that action state of switching the character image
   
            return: True或者False

            return: True or False
        """
        return "true" in self.SendData("getSwitchActionState") 

    def make_clone_audio(self, clone_server_ip: str, refer_audio_path: str, refer_text: str, clone_text: str, save_audio_path: str) -> bool:
        """
            克隆声音，需要部署服务端
            To clone sound, you need to deploy the server.

            clone_server_ip: 克隆声音服务端IP
            refer_audio_path: 参考音频路径，10-40秒，推荐25秒左右的参考音频
            refer_text: 参考音频对应的文本
            clone_text: 要克隆的文本
            save_audio_path: 保存克隆声音的路径
            return: True或者False

            clone_server_ip: clone voice server IP
            refer_audio_path: Reference audio path, 10-40 seconds, 25 seconds is recommended
            refer_text: the text corresponding to the reference audio
            clone_text: the text to be cloned
            save_audio_path: the path to save the cloned sound
            return: True or False
        """
        return "true" in self.SendData("makeCloneAudio", clone_server_ip, refer_audio_path, refer_text, clone_text, save_audio_path)


    def make_clone_lab(self, lab_server_ip: str, audio_path: str) -> bool:
        """
            生成lab文件，需要部署服务端
            To generate lab files, you need to deploy the server.

            lab_server_ip: 保存的发音文件路径。这里是路径，不是目录！
            audio_path: 要转换语音的文本
            return: True或者False

            lab_server_ip: saved pronunciation file path. This is a path, not a directory
            audio_path: the text to be converted into speech
            return: True or False
        """
        return "true" in self.SendData("makeCloneLab", lab_server_ip, audio_path) 

    def clone_audio_to_text(self, lab_server_ip: str, audio_path: str) -> bool:
        """
            语音识别，需要部署服务端
            Speech recognition requires the deployment of the server.

            lab_server_ip: lab服务端IP
            audio_path: 音频文件
            return: 失败返回None, 成功返回识别到的内容

            lab_server_ip: lab server IP
            audio_path: audio file
            return: None is returned in case of failure, and the recognized content is returned successfully
        """
        return "true" in self.SendData("cloneAudioToText", lab_server_ip, audio_path)
    
    def text_to_audio_and_lab_file(self, save_audio_path: str, text: str, language: str = "zh-cn", voice_name: str = "", quality: int = 0, speech_rate: int = 0, voice_style: str = "General") -> bool:
        """
            文本合成语音保存到本地音频文件
            Text synthesis speech is saved to a local audio file

            save_audio_path: 保存的音频文件路径，扩展为.MP3格式。同名的 .lab文件需要和音频文件在同一目录下
            text: 要转换语音的文本
            language: 语言，参考开发文档 语言和发音人
            voice_name: 发音人，参考开发文档 语言和发音人
            quality: 音质，0低品质  1中品质  2高品质， 默认为0低品质
            speech_rate: 语速，默认为0，取值范围 -100 至 200
            voice_style: 语音风格，默认General常规风格，其他风格参考开发文档 语言和发音人
            return: True或者False

            save_audio_path: the path of the saved audio file, expanded to .mp3 format. The. lab file with the same name needs to be in the same directory as the audio file
            text: the text to be converted into speech
            language: language, reference development document language and speaker
            voice_name: speaker, refer to the development document language and speaker
            quality: sound quality, 0 low quality 1 medium quality 2 high quality, and 0 low quality by default
            speech_rate: speech speed, which is 0 by default, and the value range is -100 to 200
            voice_style: voice style, the default General style, and other styles refer to the development document language and speaker
            return: True or False
        """
        return "true" in self.SendData("textToAudioAndLabFile", save_audio_path, text, language, voice_name, quality, speech_rate, voice_style)