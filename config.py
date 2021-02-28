import os

tools_cfg = {
    "Base_cfg":{
        "info":{
            "show_process":True,
            "print_process":True,
        },
    },
    "FTV_cfg": {
        "video_info": {
            "fps": 30,
            "codec": "DIVX",
        },
        "paths": {
            "file_name": "output",
            "format": "mp4",
            "frames_path": f"{os.path.dirname(os.path.realpath(__file__))}\\frames\\",
        },
    },
    "VTF_cfg": {
        "paths": {
            "file_name": "source",
            "format": "mp4",
            "frames_path": f"{os.path.dirname(os.path.realpath(__file__))}\\frames\\",
        },
    },
}
