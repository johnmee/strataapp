#!/bin/sh
git push "$@" && ssh norry 'cd /home/john/strataapp/ && git pull && git submoddule update --remote && sudo systemctl reload nginx'
