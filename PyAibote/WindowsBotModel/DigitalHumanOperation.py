import re


class DigitalHumanOperation:
    """
        数字人
        Digital human
    """

    def init_metahuman(self, metahuman_mde_path: str, metahuman_scale_value: int, is_update_metahuman: bool = False) -> bool:
        """
            初始化数字人，第一次初始化需要一些时间
            Initializing digital people, it takes some time to initialize for the first time.

            metahuman_mde_path: 数字人模型路径
            metahuman_scale_value: 数字人缩放倍数，1为原始大小。为0.5时放大一倍，2则缩小一半
            is_update_metahuman: 是否强制更新，默认fasle。为true时强制更新会拖慢初始化速度
            return: True或者False

            metahuman_mde_path: Digital human model path
            metahuman_scale_value: Digital people zoom multiple, 1 is the original size. When it is 0.5, it is doubled, and when it is 2, it is halved
            is_update_metahuman: Whether to force update, fasle by default. When true, forcing the update will slow down the initialization speed
            return: True or False
        """
        return "true" in self.SendData("initMetahuman", metahuman_mde_path, metahuman_scale_value,is_update_metahuman) 

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
        return  "true" in self.SendData("metahumanSpeech", save_voice_folder, text, language, voice_name, quality,wait_play_sound, speech_rate, voice_style) 

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
