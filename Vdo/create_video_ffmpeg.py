# run: python create_video_ffmpeg.py

import subprocess


# ============================================================
# FUNCTION: Get video duration
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
# GENERAL SETTINGS
# ============================================================

# Canvas
canvas_width = 1280
canvas_height = 720

# Video size and position
video_width = 700
video_height = 394
video_x = 10
video_y = 80

# Text position
text_x = 740
text_y = 120

# Text size
font_size = 36


# ============================================================
# SLIDE 1
# ============================================================

video1 = "1.mp4"

text1 = """Welcome
- CSCI 101 
  Computer Science I
- Fall 2026
- I am Murtaza Khan, 
- Your Instructor"""

# ============================================================
# SLIDE 2
# ============================================================

video2 = "2.mp4"

text2 = """About me
- Ph.D. Engineering,
  Keio University, Japan
  Image/Video Compression
- Database
- Data analytics
- Computer Graphics
- AI"""


# ============================================================
# CREATE ONE SLIDE
# ============================================================

def create_slide(input_video, text, output_video):

    duration = get_video_duration(input_video)

    filter_complex = (
        f"[0:v]scale={video_width}:{video_height}[video];"

        f"color=c=black:"
        f"s={canvas_width}x{canvas_height}:"
        f"d={duration}[bg];"

        f"[bg][video]overlay={video_x}:{video_y}[v];"

        f"[v]drawtext="
        f"text='{text}':"
        f"x={text_x}:"
        f"y={text_y}:"
        f"fontsize={font_size}:"
        f"fontcolor=white:"
        f"line_spacing=10[vout]"
    )

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

    subprocess.run(command, check=True)


# ============================================================
# CREATE SLIDE 1
# ============================================================

create_slide(
    video1,
    text1,
    "slide1.mp4"
)


# ============================================================
# CREATE SLIDE 2
# ============================================================

create_slide(
    video2,
    text2,
    "slide2.mp4"
)


print("\nSlide 1 and Slide 2 created successfully.")