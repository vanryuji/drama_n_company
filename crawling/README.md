# Overview
selenium과 크롬을 이용한 다이나믹 웹페이지 크롤링

# Environments
* Ubuntu 18.04
* Python 3.6
* selenium
* pyvirtualdisplay
* Google Chrome 73.0.3683.103
```shell
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
dpkg -i google-chrome-stable_current_amd64.deb
```
* Google Chrome Driver 73.0.3683.68
```shell
# Check driver version compatitable with Google Chome
# https://sites.google.com/a/chromium.org/chromedriver/downloads

wget https://chromedriver.storage.googleapis.com/73.0.3683.68/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
```
* Xbfs



# Trouble-shooting
### 1. Error on installing Google Chrome
##### 1) Error message
```shell
...
dpkg: dependency problems prevent configuration of google-chrome-stable:
...
dpkg: error processing package google-chrome-stable (--install):
 dependency problems - leaving unconfigured
Processing triggers for man-db (2.8.3-2ubuntu0.1) ...
Processing triggers for mime-support (3.60ubuntu1) ...
Errors were encountered while processing:
 google-chrome-stable
```
##### 2) Solution
refer : https://askubuntu.com/questions/214746/how-to-run-apt-get-install-to-install-all-dependencies
```shell
apt-get install -f
```


### 2. webdriver.Chrome() error!!!
##### 1) Error message:
```shell
Traceback (most recent call last):
  File "crawling.py", line 7, in <module>
    driver = webdriver.Chrome('./chromedriver')
  File "/home/ryujivan316_test/coin/lib/python3.6/site-packages/selenium/webdriver/chrome/webdriver.py", line 81, i
n __init__
    desired_capabilities=desired_capabilities)
  File "/home/ryujivan316_test/coin/lib/python3.6/site-packages/selenium/webdriver/remote/webdriver.py", line 157, 
in __init__
    self.start_session(capabilities, browser_profile)
  File "/home/ryujivan316_test/coin/lib/python3.6/site-packages/selenium/webdriver/remote/webdriver.py", line 252, 
in start_session
    response = self.execute(Command.NEW_SESSION, parameters)
  File "/home/ryujivan316_test/coin/lib/python3.6/site-packages/selenium/webdriver/remote/webdriver.py", line 321, 
in execute
    self.error_handler.check_response(response)
  File "/home/ryujivan316_test/coin/lib/python3.6/site-packages/selenium/webdriver/remote/errorhandler.py", line 24
2, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.WebDriverException: Message: unknown error: Chrome failed to start: exited abnormally
  (unknown error: DevToolsActivePort file doesn't exist)
  (The process started from chrome location /usr/bin/google-chrome is no longer running, so ChromeDriver is assumin
g that Chrome has crashed.)
  (Driver info: chromedriver=73.0.3683.68 (47787ec04b6e38e22703e856e101e840b65afe72),platform=Linux 4.15.0-1029-gcp
 x86_64)
```
##### 2) Solution:
```
/opt/google/chrome/google-chrome 
[13823:13823:0408/065157.631120:ERROR:zygote_host_impl_linux.cc(89)] Running as root without --no-sandbox is not supported. See https://crbug.com/638180.
```
google-chrome doesn't allow root user by default.<br>
Add '--no--sandbox' option.

```
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
driver = webdriver.Chrome('./chromedriver', chrome_options=options)
```



