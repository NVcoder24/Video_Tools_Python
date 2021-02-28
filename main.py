import cv2
import os
from config import tools_cfg

fps = tools_cfg["FTV_cfg"]["video_info"]["fps"]

files = []

path = tools_cfg["FTV_cfg"]["paths"]["frames_path"]
i = 0

print("--- FINDING FRAMES ---")
while True:
    if os.path.isfile(f"{path}frame_{i}.png"):
        files.append(f"{path}frame_{i}.png")
        print(f"Found frame: frame_{i}.png")
        i += 1
    else:
        break

i = 0

frames = []

print("--- WRITING FRAMES IN RAM ---")
for file in files:
    try:
        img = cv2.imread(file)
        cv2.imshow("Current frame - writing frames in RAM", img)
        if cv2.waitKey(10) == 27:
            cv2.destroyAllWindows()
            break
        height, width, layers = img.shape
        size = (width, height)
        frames.append(img)
        print(f"Writing frame in RAM: {i} ({file})")
        i += 1
    except Exception as e:
        pass

print("--- WRITING VIDEO ---")
result = cv2.VideoWriter(f"{tools_cfg['FTV_cfg']['paths']['file_name']}.{tools_cfg['FTV_cfg']['paths']['format']}",cv2.VideoWriter_fourcc(*f"{tools_cfg['FTV_cfg']['video_info']['codec']}"), fps, size)

for frame in range(len(frames)):
    print(f"Writing frame in video file: {frame}")
    result.write(frames[frame])

print("Finish!")
quit(666)
