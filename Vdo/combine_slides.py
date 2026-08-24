# run: python combine_slides.py
#
# Combines the individual slide videos into one lecture video.
#
# The individual slides must already exist.
# ============================================================

import subprocess


# ------------------------------------------------------------
# List of slides in the desired order
# ------------------------------------------------------------

slides = [
    "slide1.mp4",
    "slide2.mp4",
]


# ------------------------------------------------------------
# Create FFmpeg concat file
# ------------------------------------------------------------

with open("slides.txt", "w", encoding="utf-8") as file:

    for slide in slides:
        file.write(f"file '{slide}'\n")


# ------------------------------------------------------------
# Combine slides
#
# -c copy means FFmpeg does NOT re-encode the videos.
# This should be very fast.
# ------------------------------------------------------------

command = [
    "ffmpeg",
    "-f", "concat",
    "-safe", "0",
    "-i", "slides.txt",
    "-c", "copy",
    "-y",
    "final_lecture.mp4"
]


subprocess.run(command, check=True)


print("\nCreated: final_lecture.mp4")
