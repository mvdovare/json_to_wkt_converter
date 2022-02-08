# geojson to wkt_ test_from any of both.ipynb

import json
#import geojson
from shapely.geometry import shape

with open('any of both.json') as json_file:
    data_from_json = json.load(json_file)

if "geo_shape" in data_from_json:
    required_field = {
        "coordinates": data_from_json["geo_shape"]["best.geo"]["shape"]["coordinates"],
        "type": data_from_json["geo_shape"]["best.geo"]["shape"]["type"]
    }
else:
    required_field = data_from_json

geom = shape(required_field)

# to get a WKT/WKB representation
WKT_geo = geom.wkt
print(WKT_geo)

# # save WKT file to import into BO
# with open('WKT_geo_BO.wkt', 'w') as f:
#     f.write(WKT_geo)
#
# # save WKT file to open in QGIS
# with open('JSON boundary from EL_QGIS_3.wkt', 'w') as f:
#     f.write('\"geo\"' + '\n\"' + WKT_geo + '\"')