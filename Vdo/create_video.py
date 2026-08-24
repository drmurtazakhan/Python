# run: python create_video.py

from moviepy import VideoFileClip, TextClip, CompositeVideoClip

# -----------------------------
# Settings
# -----------------------------

CANVAS_WIDTH = 1280
CANVAS_HEIGHT = 720

VIDEO_WIDTH = 640
VIDEO_HEIGHT = 360

VIDEO_X = 40
VIDEO_Y = 180

TEXT_X = 720
TEXT_Y = 120
TEXT_WIDTH = 500
TEXT_HEIGHT = 500

# -----------------------------
# Load video
# -----------------------------

video = VideoFileClip("1.mp4")

# -----------------------------
# Create text
# -----------------------------

text = TextClip(
    text="Introduction\n\n• First point\n• Second point\n• Third point",
    font_size=36,
    color="white",
    size=(TEXT_WIDTH, TEXT_HEIGHT),
    method="caption"
).with_duration(video.duration)

# -----------------------------
# Position objects
# -----------------------------

video = video.with_position((VIDEO_X, VIDEO_Y))
text = text.with_position((TEXT_X, TEXT_Y))

# -----------------------------
# Create composition
# -----------------------------

final = CompositeVideoClip(
    [video, text],
    size=(CANVAS_WIDTH, CANVAS_HEIGHT)
)

# -----------------------------
# Export
# -----------------------------

final.write_videofile(
    "test1.mp4",
    fps=30,
    codec="libx264",
    audio_codec="aac"
)