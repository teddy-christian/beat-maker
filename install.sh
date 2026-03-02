#!/usr/bin/env bash
# ─────────────────────────────────────────────────────────
#  MrBeat — installer
#  Supports: macOS (Intel + Apple Silicon) and Linux
# ─────────────────────────────────────────────────────────
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="$SCRIPT_DIR/venv"

echo ""
echo "╔═══════════════════════════════════════╗"
echo "║        MrBeat — Installer             ║"
echo "╚═══════════════════════════════════════╝"
echo ""

# ── 1. Detect OS ──────────────────────────────────────────
OS="$(uname -s)"
echo "► Detected OS: $OS"

# ── 2. Install PortAudio (needed by sounddevice / PyAudio) ────────────
echo ""
echo "► Checking PortAudio..."

if [ "$OS" = "Darwin" ]; then
    if ! command -v brew &>/dev/null; then
        echo "✗  Homebrew not found. Install it first:"
        echo "   /bin/bash -c \"\$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\""
        exit 1
    fi
    brew install portaudio 2>/dev/null || true
    echo "  ✓ PortAudio ready (via Homebrew)"

elif [ "$OS" = "Linux" ]; then
    if command -v apt-get &>/dev/null; then
        sudo apt-get update -qq
        sudo apt-get install -y libportaudio2 portaudio19-dev
        echo "  ✓ PortAudio ready (via apt-get)"
    else
        echo "  ⚠ Unknown package manager. Make sure portaudio is installed."
    fi
fi

# ── 3. Set up Python virtual environment ─────────────────
echo ""
echo "► Setting up Python virtual environment..."

if [ ! -d "$VENV_DIR" ]; then
    python3 -m venv "$VENV_DIR"
    echo "  ✓ Virtual environment created"
else
    echo "  ✓ Virtual environment already exists"
fi

source "$VENV_DIR/bin/activate"

# ── 4. Upgrade pip ────────────────────────────────────────
pip install --quiet --upgrade pip setuptools wheel

# ── 5. Install Python dependencies ────────────────────────
echo ""
echo "► Installing Python dependencies..."
pip install --quiet -r "$SCRIPT_DIR/requirements.txt"
echo "  ✓ All dependencies installed"

# ── 6. Done ───────────────────────────────────────────────
echo ""
echo "╔═══════════════════════════════════════╗"
echo "║  ✓  Installation complete!            ║"
echo "║                                       ║"
echo "║  Run:  source venv/bin/activate       ║"
echo "║        python main.py                 ║"
echo "╚═══════════════════════════════════════╝"
echo ""
