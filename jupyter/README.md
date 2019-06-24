# Overview
jupyter 설치 방법

# Environments
* Ubuntu 14.04(remote server)
* Python 3.4
* Jupyter 4.4.0


# Install
### 1. Install jupyter
```shell
root@ubuntu1:~/dynamic_page_crawling# pip3 install jupyter
```
### 2. Create configuration
```shell
root@ubuntu1:~/dynamic_page_crawling# jupyter notebook --generate-config
Writing default config to: /root/.jupyter/jupyter_notebook_config.py
```
### 3. Edit configuration file(jupyter_notebook_config.py)
```shell
c.NotebookApp.ip = 'your_remote_server_ip' # for remote server, if you setup jupyter for localhost then just write 'localhost'
c.NotebookApp.allow_root = True # for root user
```


### 4. Run jupyter using specific configuration
```shell
root@ubuntu1:~/dynamic_page_crawling# jupyter notebook --config /root/.jupyter/jupyter_notebook_config.py
```



# Jupyter nbextensions
### 1. Install jupyter nbextensions
```shell
pip3 install jupyter_contrib_nbextensions
```


### 2. Install javascript and css files
```shell
jupyter contrib nbextension install --user
```

### 3. Enabling/Disabling extensions
```shell
# toc2
jupyter nbextension enable toc2/main
```



# Reference
* Installing guide : http://goodtogreate.tistory.com/entry/IPython-Notebook-%EC%84%A4%EC%B9%98%EB%B0%A9%EB%B2%95
* Jupyter nbextensions : https://github.com/ipython-contrib/jupyter_contrib_nbextensions
