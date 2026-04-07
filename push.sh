#!/bin/sh
git push "$@" && ssh norry 'cd /home/john/strataapp/ && git pull && git submodule update --remote && cd blog && hugo && sudo systemctl reload nginx'
