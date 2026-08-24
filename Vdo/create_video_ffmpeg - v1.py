# run: python create_video_ffmpeg.py

import subprocess

# ============================================================
# SETTINGS
# ============================================================

input_video = "1.mp4"
output_video = "test_ffmpeg.mp4"

# Canvas size
canvas_width = 1280
canvas_height = 720

# Video size and position
video_width = 700
video_height = 394
video_x = 40        #  move video left/right
video_y = 80       # move video up/down

# Text position
text_x = 760        # move text left/right   
text_y = 120        # move text up/down

# Text size
font_size = 36

# Text content
text = """Welcome
- CSCI 101 
  Computer Science I
- Fall 2026
- I am Murtaza Khan, 
- Your Instructor"""


# ============================================================
# FFMPEG FILTER
# ============================================================

filter_complex = (
    f"[0:v]scale={video_width}:{video_height}[video];"
    f"color=c=black:s={canvas_width}x{canvas_height}:d=53.675[bg];"
    f"[bg][video]overlay={video_x}:{video_y}[v];"
    f"[v]drawtext=text='{text}':"
    f"x={text_x}:y={text_y}:"
    f"fontsize={font_size}:"
    f"fontcolor=white:"
    f"line_spacing=10[vout]"
)


# ============================================================
# FFMPEG COMMAND
# ============================================================

command = [
    "ffmpeg",
    "-i", input_video,
    "-filter_complex", filter_complex,
    "-map", "[vout]",
    "-map", "0:a?",
    "-c:v", "libx264",
    "-c:a", "aac",
    "-y",
    output_video
]


# ============================================================
# RUN FFMPEG
# ============================================================

subprocess.run(command, check=True)

print(f"\nCreated: {output_video}")
