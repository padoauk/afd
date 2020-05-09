# non-standard python modules necessary for afd
- pyyaml
- requests

# installation
```
pip install PyYAML
pip install requests  
```

# notice
The python enviroment can be inkscape specific. Clarify which python inkscape uses and install the necessary modules to that python. One can use comment lines in afd.py tho get the version and the module path. 

# example
```
$ pip3 install PyYAML
Collecting PyYAML
  Downloading PyYAML-5.3.1.tar.gz (269 kB)
     |████████████████████████████████| 269 kB 6.7 MB/s 
Installing collected packages: PyYAML
    Running setup.py install for PyYAML ... done
Successfully installed PyYAML-5.3.1
```

```
# pip3 install requests
Collecting requests
  Downloading requests-2.23.0-py2.py3-none-any.whl (58 kB)
     |████████████████████████████████| 58 kB 6.3 MB/s 
Collecting chardet<4,>=3.0.2
  Downloading chardet-3.0.4-py2.py3-none-any.whl (133 kB)
     |████████████████████████████████| 133 kB 14.7 MB/s 
Collecting idna<3,>=2.5
  Downloading idna-2.9-py2.py3-none-any.whl (58 kB)
     |████████████████████████████████| 58 kB 12.7 MB/s 
Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in /Users/ici/.pyenv/versions/3.7.6/lib/python3.7/site-packages (from requests) (1.25.9)
Collecting certifi>=2017.4.17
  Downloading certifi-2020.4.5.1-py2.py3-none-any.whl (157 kB)
     |████████████████████████████████| 157 kB 24.7 MB/s 
Could not build wheels for urllib3, since package 'wheel' is not installed.
Installing collected packages: chardet, idna, certifi, requests
Successfully installed certifi-2020.4.5.1 chardet-3.0.4 idna-2.9 requests-2.23.0
```