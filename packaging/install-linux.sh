#!/usr/bin/env bash
set -e

BINARY="beat-maker-linux"
INSTALL_DIR="$HOME/.local/bin"
DESKTOP_DIR="$HOME/.local/share/applications"
INSTALL_PATH="$INSTALL_DIR/beat-maker"

# ── Locate binary ───────────────────────────────────────────────────────────
if [[ ! -f "$BINARY" ]]; then
  echo "Error: '$BINARY' not found. Run this script from the same folder as the binary."
  exit 1
fi

# ── Install ─────────────────────────────────────────────────────────────────
mkdir -p "$INSTALL_DIR" "$DESKTOP_DIR"

echo "Installing binary to $INSTALL_PATH ..."
cp "$BINARY" "$INSTALL_PATH"
chmod +x "$INSTALL_PATH"

echo "Creating desktop entry ..."
cat > "$DESKTOP_DIR/beat-maker.desktop" << DESKTOP
[Desktop Entry]
Version=1.0
Type=Application
Name=MrBeat
Comment=Drum machine and beat maker
Exec=$INSTALL_PATH
Icon=audio-x-generic
Terminal=false
Categories=AudioVideo;Music;
Keywords=beat;drum;music;sequencer;
StartupWMClass=beat-maker
DESKTOP

update-desktop-database "$DESKTOP_DIR" 2>/dev/null || true

echo ""
echo "✓ MrBeat installed!"
echo "  Binary : $INSTALL_PATH"
echo "  Launcher: $DESKTOP_DIR/beat-maker.desktop"
echo ""
echo "You can now launch it from your application menu or run: beat-maker"
