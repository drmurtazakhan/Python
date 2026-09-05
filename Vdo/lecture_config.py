# run: python lecture_config.py

# This file contains the CONTENT and LAYOUT settings
# for the lecture.
#
# Normally, you will NOT need to change create_slides.py.
# ============================================================


# ------------------------------------------------------------
# OUTPUT CANVAS
# ------------------------------------------------------------

CANVAS_WIDTH = 1280
CANVAS_HEIGHT = 720

TEXT_WIDTH = 450

# ------------------------------------------------------------
# VIDEO SIZE AND POSITION
#
# These settings are currently the same for every slide.
# ------------------------------------------------------------

VIDEO_WIDTH = 700
VIDEO_HEIGHT = 394

VIDEO_X = 10
VIDEO_Y = 80


# ------------------------------------------------------------
# TEXT POSITION AND SIZE
# ------------------------------------------------------------

TEXT_X = 740
TEXT_Y = 120

FONT_SIZE = 36

# ============================================================
# SLIDE CONTENT
# ============================================================
SLIDES = {
    # ------------------------------------------------------------
    # SLIDE 1
    # ------------------------------------------------------------

    1: {
        "video": "1.mp4",

        "text": """Welcome
- CSCI 101 
  Computer Science I
- Fall 2026
- I am Murtaza Khan, 
- Your Instructor"""
    },

    # ------------------------------------------------------------
    # SLIDE 2
    # ------------------------------------------------------------

    2: {
        "video": "2.mp4",

        "text": """About me
- Ph.D. Engineering,
  Keio University, Japan
  Image/Video Compression
- Database
- Data analytics
- Computer Graphics
- AI"""
    },

    3: {
        "video": "3.mp4",

        "text": """Schedule
- Two virtual classes
- via Zoom
- Tuesday and Thursday,
- 6\:00 pm - 7\:45 pm"""
    },

    4: {
        "video": "4.mp4",

        "text": """C++ programming Topics
- Data types
- Control structures
- Functions
- Arrays 
- File I/O
- Testing and Debugging"""
    },

    5: {
        "video": "5.mp4",

        "text": """Expectations & Policies
- Be engaged
- Stay organized
- Class activities
- Syllabus
- IvyLearn calendar
- Assignments on time
- Communicate"""
    },

    6: {
        "video": "6.mp4",

        "text": """Let’s work together
to make this semester
a positive, 
engaging, and
rewarding experience."""
    },

}
