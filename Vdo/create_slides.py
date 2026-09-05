# run: python create_slides.py
#
# Creates selected slide videos using FFmpeg.
#
# The slide content and layout are obtained from
# lecture_config.py.
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
    SLIDES
)


# ============================================================
# WHICH SLIDES SHOULD BE CREATED?
#
# Examples:
#
# slides_to_create = [2]
#       Creates only Slide 2
#
# slides_to_create = [1, 3, 5]
#       Creates Slides 1, 3 and 5
#
# slides_to_create = "all"
#       Creates every slide in SLIDES
# ============================================================

slides_to_create = [6]  # Change this to the slides you want to create


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
# CREATE ONE SLIDE
# ============================================================

def create_slide(slide_number, slide):

    input_video = slide["video"]
    text = slide["text"]

    output_video = f"slide{slide_number}.mp4"

    print()
    print("=" * 60)
    print(f"Creating Slide {slide_number}")
    print(f"Input : {input_video}")
    print(f"Output: {output_video}")
    print("=" * 60)

    # --------------------------------------------------------
    # Get actual video duration
    # --------------------------------------------------------

    duration = get_video_duration(input_video)

    # --------------------------------------------------------
    # Create FFmpeg filter
    # --------------------------------------------------------

    filter_complex = (

        # Resize lecture video
        f"[0:v]scale={VIDEO_WIDTH}:{VIDEO_HEIGHT}[video];"

        # Create background
        f"color=c=black:"
        f"s={CANVAS_WIDTH}x{CANVAS_HEIGHT}:"
        f"d={duration}[bg];"

        # Place video on background
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

    # --------------------------------------------------------
    # Run FFmpeg
    # --------------------------------------------------------

    subprocess.run(command, check=True)

    print(f"Finished Slide {slide_number}")


# ============================================================
# DETERMINE WHICH SLIDES TO CREATE
# ============================================================

if slides_to_create == "all":

    selected_slides = SLIDES.keys()

else:

    selected_slides = slides_to_create


# ============================================================
# CREATE SELECTED SLIDES
# ============================================================

for slide_number in selected_slides:

    if slide_number not in SLIDES:
        print(f"WARNING: Slide {slide_number} does not exist.")
        continue

    create_slide(
        slide_number,
        SLIDES[slide_number]
    )


print()
print("Selected slides have been created.")
