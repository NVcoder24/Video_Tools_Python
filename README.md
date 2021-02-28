# Video_Tools_Python
video tools!

## Libraries (PIP)
```bash
pip install opencv-python
```

## Usage
1. put you video in directory with VTF py file
###### it must look like this:
![image](https://github.com/NVcoder24/Video_Tools_Python/blob/resources/step1.png?raw=true)
2. run "video to frames.py"
3. frames will be save in frames folder

## Config
```python
import os

tools_cfg = {
    # Base config
    "Base_cfg":{
        "info":{
            "show_process":True,  # show processing frame (in new window)
            "print_process":True, # show processing frame (in the console)
        },
    },
    # Frames To Video config
    "FTV_cfg": {
        "video_info": {
            "fps": 30,       # Frames Per Second
            "codec": "DIVX", # Video codec (default - DIVX)
        },
        "paths": {
            "file_name": "output", # video name
            "format": "mp4",       # video format
            "frames_path": f"{os.path.dirname(os.path.realpath(__file__))}\\frames\\", # frames path
        },
    },
    # Video To Frames config
    "VTF_cfg": {
        "paths": {
            "file_name": "source", # video name
            "format": "mp4",       # video format
            "frames_path": f"{os.path.dirname(os.path.realpath(__file__))}\\frames\\", # path for frames
        },
    },
}

```
