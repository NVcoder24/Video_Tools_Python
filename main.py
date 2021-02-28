import cv2
import os
from config import tools_cfg

show_p = tools_cfg["Base_cfg"]["info"]["show_process"]
print_p = tools_cfg["Base_cfg"]["info"]["print_process"]

vidcap = cv2.VideoCapture(f"{tools_cfg['VTF_cfg']['paths']['file_name']}.{tools_cfg['VTF_cfg']['paths']['format']}")
success,image = vidcap.read()
count = 0
count_ = 1
success = True
path = tools_cfg['VTF_cfg']['paths']['frames_path']
length = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = vidcap.get(cv2.CAP_PROP_FPS)
height = vidcap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = vidcap.get(cv2.CAP_PROP_FRAME_WIDTH)

iff = lambda value : str(value)[:str(value).index('.')]
find_procent = lambda value, max : value * 100 / max

length_sec = iff(length / fps)

try:
    os.mkdir(path)
except Exception as e:
    pass

print(f"--- VIDEO INFORMATION ---\nvideo length (in frames): {length}\nvideo FPS: {fps}\nvideo length (in sec): {length_sec}\nvideo resolution: {iff(width)}px/{iff(height)}px ({iff(height)}p)\n-------------------------")
input("Press Enter to begin!")


while success:
    success,image = vidcap.read()
    try:
        cv2.imwrite(f"{path}frame_{count}.png", image)
        count__ = find_procent(count_, length)
        if print_p:
            print(f"Frame {count} saved! ({iff(count__)}%)")
        if show_p:
            cv2.imshow(f"Current frame", image)
        if cv2.waitKey(10) == 27:
            cv2.destroyAllWindows()
            break
        count += 1
        count_ += 1
    except Exception as e:
        print("Finish!")
        quit(666)
