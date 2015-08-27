#!/usr/bin/env bash

function _exit() { echo "$1" 1>&2 ; exit 1; }
function _require() { type "$1" 1>/dev/null 2>/dev/null || _exit "$1 required"; }

_require i3-msg
_require jshon
_require tr

function _i3_get_outputs() {
  echo "$(i3-msg -t get_outputs)"
}

function _i3_get_workspace() {
  echo "$(_i3_get_outputs)" | jshon -e "$1" | jshon -e current_workspace | tr -d '"'
}

function _i3_move_workspace() {
  i3-msg "workspace $1" >/dev/null 2>&1
  i3-msg "move workspace to output right" >/dev/null 2>&1
}

W1="$(_i3_get_workspace 0)"
W2="$(_i3_get_workspace 1)"

_i3_move_workspace "$W1"
sleep 0.01
_i3_move_workspace "$W2"

exit 0
