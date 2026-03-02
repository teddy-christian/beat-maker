[app]
title = MrBeat
package.name = mrbeat
package.domain = com.teddychristian
source.dir = ..
source.include_exts = py,kv,wav
source.include_patterns = sounds/kit1/*.wav,*.kv
version = 1.0.0

# pyjnius>=1.5.0 fixes the Python-3-incompatible 'long' type error
requirements = python3,kivy==2.3.0,pyjnius>=1.5.0

orientation = landscape
fullscreen = 0

android.permissions = INTERNET
android.api = 33
android.minapi = 26
android.ndk = 27
android.archs = arm64-v8a,armeabi-v7a
android.accept_sdk_license = True
android.allow_backup = False
android.release_artifact = apk
android.logcat_filters = *:S python:D

# Re-use the SDK/NDK already installed on the GitHub Actions runner
# so buildozer doesn't download ~1 GB of toolchain
android.sdk_path = /usr/local/lib/android/sdk
android.ndk_path = /usr/local/lib/android/sdk/ndk/27.3.13750724

[buildozer]
log_level = 2
warn_on_root = 1
