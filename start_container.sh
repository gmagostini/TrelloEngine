#!/usr/bin/env bash
porta=8080
docker image build -t "trelloengine:test" . 
echo "=============================================================="
echo "[START SERVER]listening on http://0.0.0.0:$porta/"
docker run --rm --name "TrelloTest" -p $porta:8080 trelloengine:test