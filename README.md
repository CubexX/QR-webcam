# RTQR
A simple real time QR and Bar code recognition using Python. This will connect to your webcam and constantly scan for any QR or bar codes. If one is detected, it'll translate it for you in the output.  

# Dependencies
Python 3, ZBar, OpenCV and PIL.

# Usage
```python
from RTQR import decode


def main():
    qr = decode()
    print(qr)


if __name__ == "__main__":
    main()
```

# Install
```bash
# apt-get install opencv
# apt-get install zbar
```

```bash
# pip install git+https://github.com/CubexX/QR-webcam.git
```
