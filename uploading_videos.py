import os

def collect_video_paths(root_folder):
    video_paths = []
    for root, dirs, files in os.walk(root_folder):
        for file in files:
            if file.endswith('.mp4'):
                video_paths.append(os.path.join(root, file))
    return video_paths

extracted_folder_path = '/kaggle/input/{name_of_dataset}'

video_paths = collect_video_paths(extracted_folder_path)

for path in video_paths:
    print(path)