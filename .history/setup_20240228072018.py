from setuptools import setup, find_packages

packages = find_packages()
install_requires = [
    "loguru",
    "psutil",
    "Pillow",
    "requests"
]

setup(
    name="PyAibote", 
    version="1.2.2", 
    author="Riven", 
    author_email="pyaibote@163.com", 
    description="A pure code RPA office automation framework, which supports Android, Browser and Windows", 
    long_description="Support Android native APP and H5 interface elements and color positioning. The speed of element location is 10 times that of Appium framework, and the color location of 2340*1080 image only takes 50 milliseconds, It supports the positioning of window interface elements and colors developed by Windows applications,. NET, WinForm, WPF, QT, Java (GUI libraries such JAVA(Swing and AWT) and Electron. The exclusive xpath algorithm is concise and rapid, and the positioning speed of elements/colors is 3 times and 20 times that of visual RPA, respectively, All browsers and applications that support the chromium kernel. A web automation framework developed by C/C++ language based on browser kernel protocol. Ten times faster than Selenium", # 加载read_me的内容
    long_description_content_type="text/markdown", 
    url="",  
    packages=packages, 
    package_data={"": ['*.py']},
    install_requires = install_requires,
    python_requires = ">=3.7,<4.0"
)