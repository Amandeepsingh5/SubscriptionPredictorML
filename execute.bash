#!/bin/bash
source ../virtualenv/bin/activate; LC_ALL=es_MX.utf8 LANG=es_MX.utf8 FLASK_APP=predictyesno FLASK_ENV=production flask run --host 0.0.0.0 --port 52154
