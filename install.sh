#!/usr/bin/env bash
# Install or update DSkills for the current user:
#   curl -fsSL https://raw.githubusercontent.com/ddofer/DSkills/main/install.sh | bash
# Clones to ~/DSkills (or pulls if it is there), then links every skill with link.sh.
set -eu
dir="${DSKILLS_DIR:-$HOME/DSkills}"
if [ -d "$dir/.git" ]; then
  git -C "$dir" pull -q --ff-only
else
  git clone -q https://github.com/ddofer/DSkills "$dir"
fi
"$dir/link.sh"
echo "Start a new agent session to load the skills."
