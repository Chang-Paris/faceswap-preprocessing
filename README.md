# faceswap-preprocessing

This repository contains helper function of face images copying and renaming.
Faceswap detects faces of each frame of video. 
In a long video where each frame contains face, several tens of thousands of face images are extracted into a single folder
, thus add pressure on PC. the Sorting functionality and manual removing of undesired faces are extremely slow.

The scripts under this repository will split whole face images set evenly to 10 chunks.
After having obtained cleaned face set with Faceswap, it renmames the face images and group all chunks back to one folder.
Then user could use Faceswap to re-generate .fsa file.

## Usage
