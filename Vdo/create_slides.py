# run: python create_slides.py
#
# Creates individual slide videos using FFmpeg.
#
# This file normally does NOT need to be edited.
# Content and layout are stored in lecture_config.py.
# ============================================================

import subprocess

from lecture_config import (
    CANVAS_WIDTH,
    CANVAS_HEIGHT,
    VIDEO_WIDTH,
    VIDEO_HEIGHT,
    VIDEO_X,
    VIDEO_Y,
    TEXT_X,
    TEXT_Y,
    FONT_SIZE,
    SLIDE_1,
    SLIDE_2
)


# ============================================================
# GET VIDEO DURATION
# ============================================================

def get_video_duration(filename):

    result = subprocess.run(
        [
            "ffprobe",
            "-v", "error",
            "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1",
            filename
        ],
        capture_output=True,
        text=True,
        check=True
    )

    return float(result.stdout.strip())


# ============================================================
# CREATE ONE SLIDE VIDEO
# ============================================================

def create_slide(slide_number, slide):

    input_video = slide["video"]
    text = slide["text"]

    output_video = f"slide{slide_number}.mp4"

    print(f"\nCreating Slide {slide_number}...")
    print(f"Video: {input_video}")

    # Get the actual duration of this video's audio/video
    duration = get_video_duration(input_video)

    # --------------------------------------------------------
    # FFmpeg filter
    # --------------------------------------------------------

    filter_complex = (

        # Resize the lecture video
        f"[0:v]scale={VIDEO_WIDTH}:{VIDEO_HEIGHT}[video];"

        # Create 1280 x 720 black background
        f"color=c=black:"
        f"s={CANVAS_WIDTH}x{CANVAS_HEIGHT}:"
        f"d={duration}[bg];"

        # Put video on the background
        f"[bg][video]"
        f"overlay={VIDEO_X}:{VIDEO_Y}[v];"

        # Add text
        f"[v]drawtext="
        f"text='{text}':"
        f"x={TEXT_X}:"
        f"y={TEXT_Y}:"
        f"fontsize={FONT_SIZE}:"
        f"fontcolor=white:"
        f"line_spacing=10[vout]"
    )

    # --------------------------------------------------------
    # FFmpeg command
    # --------------------------------------------------------

    command = [
        "ffmpeg",

        "-i", input_video,

        "-filter_complex",
        filter_complex,

        "-map", "[vout]",
        "-map", "0:a?",

        "-c:v", "libx264",
        "-c:a", "aac",

        "-y",
        output_video
    ]

    # Run FFmpeg
    subprocess.run(command, check=True)

    print(f"Created: {output_video}")


# ============================================================
# CREATE SLIDES
# ============================================================

# create_slide(1, SLIDE_1)
create_slide(2, SLIDE_2)


print("\nAll requested slides have been created.")
