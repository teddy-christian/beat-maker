# -*- mode: python ; coding: utf-8 -*-
import sys
import os
from pathlib import Path

APP_NAME = "beat-maker"
ROOT = Path(SPECPATH).parent  # repo root

a = Analysis(
    [str(ROOT / "main.py")],
    pathex=[str(ROOT)],
    binaries=[],
    datas=[
        (str(ROOT / "sounds" / "kit1"), "sounds/kit1"),
        (str(ROOT / "mrbeat.kv"),        "."),
        (str(ROOT / "track.kv"),         "."),
        (str(ROOT / "play_indicator.kv"),"."),
    ],
    hiddenimports=[
        # sounddevice / PortAudio
        "sounddevice",
        "_sounddevice_data",
        # Kivy core
        "kivy",
        "kivy._event",
        "kivy.core.window",
        "kivy.core.window.window_sdl2",
        "kivy.core.text",
        "kivy.core.text.text_sdl2",
        "kivy.core.image",
        "kivy.core.image.img_sdl2",
        "kivy.core.image.img_pil",
        "kivy.core.audio",
        "kivy.core.audio.audio_sdl2",
        "kivy.graphics",
        "kivy.graphics.cgl_backend",
        "kivy.graphics.cgl_backend.cgl_glew",
        "kivy.graphics.cgl_backend.cgl_mock",
        # App modules
        "audio_engine",
        "audio_source_mixer",
        "audio_source_one_shot",
        "audio_source_track",
        "audio_source_track",
        "thread_source",
        "sound_kit_service",
        "track",
        "play_indicator",
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=["tkinter", "matplotlib", "numpy", "scipy", "PIL.ImageQt"],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name=APP_NAME,
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # No terminal window on Windows/macOS
    icon=None,      # Set to 'packaging/beat-maker.ico' once you have an icon
    onefile=True,   # Single-file executable
)

# macOS .app bundle
if sys.platform == "darwin":
    app = BUNDLE(
        exe,
        name=f"{APP_NAME}.app",
        icon=None,
        bundle_identifier="com.teddychristian.mrbeat",
        info_plist={
            "CFBundleName": "MrBeat",
            "CFBundleDisplayName": "MrBeat",
            "CFBundleVersion": "1.0.0",
            "CFBundleShortVersionString": "1.0.0",
            "NSHighResolutionCapable": True,
            "NSMicrophoneUsageDescription": "MrBeat needs audio output access.",
        },
    )
