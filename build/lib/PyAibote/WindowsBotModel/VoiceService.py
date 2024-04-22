import re


class VoiceService:
    """
        语音服务
        Language service
    """

    def init_speech_service(self, speech_key: str, speech_region: str) -> bool:
        """
            初始化语音服务(不支持win7)，需要调用 activateSpeechService 激活
            To initialize voice service (win7 is not supported), you need to call activateSpeechService to activate it

            speech_key: 微软语音API密钥
            speech_region: 区域
            return: True或者False

            speech_key: Microsoft voice API key
            speech_region: region
            return: True or False
        """
        return "true" in self.SendData("initSpeechService", speech_key, speech_region) 

    def audio_file_to_text(self, file_path, language: str) -> str:
        """
            音频文件转文本
            Audio file to text

            file_path: 音频文件路径
            language: 语言，参考开发文档 语言和发音人 zh-cn
            return: 转换后的音频文本或者None

            file_path: the audio file path
            language: language, reference development document language and speaker zh-cn
            return: converted audio text or None
        """
        response = self.SendData("audioFileToText", file_path, language)
        if response == "null":
            return None
        return response

    def microphone_to_text(self, language: str) -> str:
        """
            麦克风输入流转换文本
            Microphone input stream conversion text

            language: 语言，参考开发文档 语言和发音人 zh-cn
            return: 转换后的音频文本或者None

            language: language, reference development document language and speaker zh-cn
            return: converted audio text or None
        """
        response = self.SendData("microphoneToText", language)
        if response == "null":
            return None
        return response

    def text_to_bullhorn(self, ssml_path_or_text: str, language: str, voice_name: str) -> bool:
        """
            文本合成音频到扬声器
            Text synthesis audio to speakers

            ssml_path_or_text: 要转换语音的文本或者".xml"格式文件路径
            language: 语言，参考开发文档 语言和发音人 zh-cn
            voice_name: 发音人，参考开发文档 语言和发音人  zh-cn-XiaochenNeural
            return: True或者False

            ssml_path_or_text: The path of the text or ".xml" format file to be converted into speech
            language: Language, reference development document language and speaker  zh-cn
            voice_name: Speaker, reference development document language and speaker zh-cn-XiaochenNeural
            return: True or False  
        """
        return "true" in self.SendData("textToBullhorn", ssml_path_or_text, language, voice_name) 

    def text_to_audio_file(self, ssml_path_or_text: str, language: str, voice_name: str, audio_path: str) -> bool:
        """
            文本合成音频并保存到文件
            Text synthesizes audio and saves it to a file.

            ssml_path_or_text: 要转换语音的文本或者".xml"格式文件路径
            language: 语言，参考开发文档 语言和发音人
            voice_name: 发音人，参考开发文档 语言和发音人
            audio_path: 保存音频文件路径
            return: True或者False

            ssml_path_or_text: the text or file path in ".xml" format to be converted
            language: language, reference development document language and speaker
            voice_name: speaker, refer to the development document language and speaker
            audio_path: the path to save the audio file
            return: True or False
        """
        return "true" in self.SendData("textToAudioFile", ssml_path_or_text, language, voice_name, audio_path) 

    def microphone_translation_text(self, source_language: str, target_language: str) -> str:
        """
            麦克风音频翻译成目标语言文本
            Microphone audio is translated into target language text

            source_language: 要翻译的语言，参考开发文档 语言和发音人
            target_language: 翻译后的语言，参考开发文档 语言和发音人
            return: 转换后的音频文本或者None

            source_language: the language to be translated, refer to the development document language and speaker
            target_language: the translated language, referring to the development document language and speaker
            return: converted audio text or None
        """
        response = self.SendData("microphoneTranslationText", source_language, target_language)
        if response == "null":
            return None
        return response

    def audio_file_translation_text(self, audio_path: str, source_language: str, target_language: str) -> str:
        """
            麦克风输入流转换文本
            Microphone input stream conversion text

            audio_path: 要翻译的音频文件路径
            source_language: 要翻译的语言，参考开发文档 语言和发音人
            target_language: 翻译后的语言，参考开发文档 语言和发音人
            return: 转换后的音频文本或者None

            audio_path: the path of the audio file to be translated
            source_language: the language to be translated, refer to the development document language and speaker
            target_language: the translated language, referring to the development document language and speaker
            return: converted audio text or None
        """
        response = self.SendData("audioFileTranslationText", audio_path, source_language, target_language)
        if response == "null":
            return None
        return response
