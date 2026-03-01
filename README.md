# MrBeat 🥁

![Screenshot](docs/screenshot.png)

> *Replace `docs/screenshot.png` with an actual screenshot of the app.*

---

## Requirements

- Python 3.11+
- A virtual environment with the dependencies below

## Setup

```bash
# Clone the repo
git clone https://github.com/teddy-christian/beat-maker.git
cd beat-maker

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install kivy sounddevice Cython
```

## Run

```bash
source venv/bin/activate
python main.py
```

## Usage

| Element | Action |
|---------|--------|
| **PLAY / STOP** buttons | Start or stop playback |
| **− / +** buttons | Decrease / increase BPM (min 80, max 160) |
| **Left button** on each track | Preview the sound once |
| **Step buttons** (16 × per track) | Toggle steps on/off for the beat |
| **Scroll** | Scroll through all 44 kit sounds |

## Project Structure

```
beat-maker/
├── main.py                  # App entry point
├── audio_engine.py          # AudioEngine (output stream setup)
├── audio_source_mixer.py    # Mixes all tracks into one stream
├── audio_source_track.py    # Single beat-sequencer track
├── audio_source_one_shot.py # One-shot sound preview
├── sound_kit_service.py     # Loads WAV files from sounds/kit1/
├── track.py / track.kv      # TrackWidget UI
├── play_indicator.py/.kv    # Step position indicator bar
├── mrbeat.kv                # Main layout
└── sounds/kit1/             # 44 drum samples
```
