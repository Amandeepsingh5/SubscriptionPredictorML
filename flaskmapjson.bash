#!/bin/bash
FLASK_DELAY_EVALUATIONS=1 LC_ALL=es_MX.utf8 LANG=es_MX.utf8 FLASK_APP=predictyesno FLASK_ENV=production flask url_map_to_json
