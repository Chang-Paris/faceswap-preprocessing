"""
Extract 10 frames randomly from each video
"""


import os
from glob import glob
import cv2
import random

random.seed(42)
SAMPLE_PER_VIDEO = 10

class Extractor:
    def __init__(self, output_folder):
        os.makedirs(output_folder, exist_ok=True)
        self.output_folder = output_folder

    def open_video(self, file_path=""):
        # read an exiting video file
        cap = cv2.VideoCapture(file_path)
        length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        return cap, length

    def sample_frame(self, cap, frame_number):
        # extract frames from random timeline
        cap.set(1, frame_number)
        _, img = cap.read()
        return img

    def write_frame(self, img, basename, frame):
        # write a frame image file to disk
        output_file = os.path.join(self.output_folder, basename+"_"+str(frame)+".png")
        cv2.imwrite(output_file, img)
        return

    def get_video_list(self, video_folder=""):
        # process all the video in the given input folder
        if not os.path.exists(video_folder):
            print("input folder does not exist ", video_folder)
        else:
            video_list = glob(video_folder+"/*.mp4")
            self.video_list = video_list

    def process_video(self):
        # process all the video in the given input folder
        for video_path in self.video_list:
            cap, length = self.open_video(file_path=video_path)
            sampled_frame = random.sample(range(length), SAMPLE_PER_VIDEO)
            for frame in sampled_frame:
                img = self.sample_frame(cap=cap, frame_number=frame)
                self.write_frame(
                    img=img,
                    basename=os.path.basename(video_path).split('.')[0],
                    frame=frame
                )

if __name__ == "__main__":
    ext = Extractor(output_folder="./output")
    ext.get_video_list(video_folder="./video")
    ext.process_video()