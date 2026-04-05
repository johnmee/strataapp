#!/bin/sh
git push "$@" && ssh norry 'cd /home/john/strataapp/src && git pull && sudo systemctl reload nginx'
