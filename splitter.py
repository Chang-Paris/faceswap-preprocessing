"""
Split all face images of a single video to chunks of folders

"""
import os
import numpy as np
import shutil


GROUP=10

class SPLITTER:
    def __init__(self, video_name, face_folder="", output_folder=""):
        print("processing video ", video_name)
        self.video_name = video_name
        self.face_folder = face_folder
        self.output_folder = output_folder
        self.file_list = []
        self.chunks=[]

    # get number of total frames
    def get_frame_number(self):
        return len(os.listdir(self.face_folder))

    def get_filelist(self):
        self.file_list = sorted(os.listdir(self.face_folder))

    # move each group's images to separate folder
    def split_to_groups(self):
        total_frame = self.get_frame_number()
        print("Total frame number is ", total_frame)
        file_index = np.arange(total_frame)
        self.chunks = np.array_split(file_index, GROUP)

    def move_to_subfolder(self):
        for chunk_group, chunk in enumerate(self.chunks):
            chunk_folder = os.path.join(self.output_folder, self.video_name+"_"+str(chunk_group))
            if os.path.exists(chunk_folder):
                shutil.rmtree(chunk_folder)
            os.makedirs(chunk_folder, exist_ok=True)
            for img_idx in chunk:
                src = os.path.join(self.face_folder, self.file_list[img_idx])
                dest = os.path.join(chunk_folder, self.file_list[img_idx])
                shutil.move(src, dest)
            print("Moved image to chunk folder : ", len(os.listdir(chunk_folder)))


target_images_folder = './face_img_chunks/'
for video_name in os.listdir(target_images_folder):
    print(video_name)
    face_folder = os.path.join(target_images_folder, video_name)

    splitter = SPLITTER(
        video_name=video_name,
        face_folder=face_folder,
        output_folder=target_images_folder
    )
    splitter.split_to_groups()
    splitter.get_filelist()
    splitter.move_to_subfolder()

