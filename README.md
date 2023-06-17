# faceswap-preprocessing

This repository contains helper function of face images copying and renaming.
Faceswap detects faces of each frame of video. 
In a long video where each frame contains face, several tens of thousands of face images are extracted into a single folder
, thus add pressure on PC. the Sorting functionality and manual removing of undesired faces are extremely slow.

The scripts under this repository will split whole face images set evenly to 10 chunks.
After having obtained cleaned face set with Faceswap, it renmames the face images and group all chunks back to one folder.
Then user could use Faceswap to re-generate .fsa file.

## Usage
### Downloader
Use this module to download all videos from excel sheet's url

### Extractor
To create a training dataset of Faceswap, use this module to randomly pick up frames from each video.
Number of face images is defined by *SAMPLE_PER_VIDEO*.

### Splitter
To clean the extracted face images of source video, use splitter to divide all face images of a large video into chunks.
The original face images are moved to chunks. The number of chunks are define in *GROUP*.
I recommend having no more than 10k face images of size 64*64 per chunk on a 32G RAM PC.

### Renamer
Run Faceswap Sorting functionality under each chunk will create sub-folders, if use "FACE" as
sorting and grouping condition, the output folder will have at least one single folder called **_face_000_by_face**.
This module will move face images of other sorted folder into **_face_000_by_face**.
It also renames face images of other sorted folder with incrementing index value starting from 
*max_index(face_000_by_face)*.

Then use Faceswap to update alignment file.
 