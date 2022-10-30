# Gmail account page autotest

Tests for enter gmail/google account. All test documentation and requiements for verification are located in the file
"Tests documentation.xlsx"

_Based on Python 3.10_

## Installing:

### Requirements:

```sh
pip install -r requirements.txt
```

### Chromium:

Download page:

``https://sites.google.com/chromium.org/driver/``

**Ubutu** install:

```sh
unzip chromedriver_linux64.zip
```

```sh
sudo mv chromedriver /usr/local/bin/chromedriver
sudo chown root:root /usr/local/bin/chromedriver
sudo chmod +x /usr/local/bin/chromedriver
```

**Windows** install:

* unzip chromedriver_win32.zip

* add directory with chromedriver.exe to PATH

## Start  all tests

```sh
pytest -v tests/
```