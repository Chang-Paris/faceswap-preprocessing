"""
Rename the cleaned face images file name and move groups of sorted images into a single folder defined by FACESWAP_SORTED_FOLDER.
Note, _face_000_by_face is the default folder name in Faceswap after sorting and grouping images by "FACE".
if use other grouping condition, modify it accordingly.

"""
import os
import shutil
from splitter import GROUP

FACESWAP_SORTED_FOLDER = "_face_000_by_face"

class RENAMER:
    def __init__(self, video_name="", image_folder=""):
        self.video_name = video_name
        self.image_folder = image_folder
        self.zero_folder = os.path.join(self.image_folder, video_name+'_0')

    def get_max_file_index(self):
        # get the max index number of file from folder 0
        face_folder = os.path.join(self.zero_folder, FACESWAP_SORTED_FOLDER)
        file_list = os.listdir(face_folder)
        index_list = []
        for file in file_list:
            current_index = int(os.path.basename(file).split("_")[0])
            index_list.append(current_index)
        return max(index_list)

    def rename_files(self, folder, starting_index, dest_folder=""):
        # rename the current folder index prefix
        # move all images to  folder
        face_folder = os.path.join(folder, FACESWAP_SORTED_FOLDER)
        file_list = sorted(os.listdir(face_folder))
        for file in file_list:
            current_index, file_basename = file.split("_", 1)
            dest_index = str(int(current_index) + starting_index).rjust(6, '0')
            dest_filename = dest_index + "_" + file_basename
            dest_url = os.path.join(dest_folder, dest_filename)
            src = os.path.join(face_folder, file)
            shutil.move(src, dest_url)

    def process_subfolder(self, folder):
        # get all subfolder list
        sub_folder_list = os.listdir(folder)
        if len(sub_folder_list) > 1:
            #  when subfolder number > 1, go into sub-sub folder
            for sub_folder in sub_folder_list:
                if sub_folder != FACESWAP_SORTED_FOLDER:
                    current_sub_folder = os.path.join(folder, sub_folder)
                    for file in os.listdir(current_sub_folder):
                        #  move all images to _face_000_by_face folder
                        src = os.path.join(current_sub_folder, file)
                        dest = os.path.join(folder+"/"+FACESWAP_SORTED_FOLDER, file)
                        shutil.move(src, dest)
                    if os.path.exists(current_sub_folder) and len(os.listdir(current_sub_folder)) == 0:
                        print("Deleting sub folder ", current_sub_folder)
                        shutil.rmtree(current_sub_folder)


if __name__ == "__main__":
    output_images = "./group_sorting/"
    video_name = "video"
    renamer = RENAMER(
        video_name=video_name,
        image_folder=output_images
    )
    max_index = renamer.get_max_file_index()

    for subfolder_index in range(int(GROUP+1)):
        subfolder = os.path.join(output_images,  video_name+"_"+str(subfolder_index))
        print("processing sub folder ", subfolder)
        if os.path.exists(subfolder):
            renamer.process_subfolder(subfolder)
            if subfolder_index != 0:
                renamer.rename_files(
                    folder=subfolder,
                    starting_index=max_index,
                    dest_folder=os.path.join(renamer.zero_folder, FACESWAP_SORTED_FOLDER)
                )
            max_index = renamer.get_max_file_index()
            print("updated max index is ", max_index)
