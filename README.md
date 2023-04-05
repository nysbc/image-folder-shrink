# image-folder-shrink

This script reduces the size of leginon image folder when there
are dose-weighted image presence.
This is done by shrinking unaligned image to 8x8 array that
retains mean and standard deviation of the original mrc image.
It also remove non dose weighted aligned file and replaces
it with a soft link to the dose-weighted version.
