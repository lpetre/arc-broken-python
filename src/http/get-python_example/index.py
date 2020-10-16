import json
import arc

def handler():
  return {'body': json.dump(arc.reflect())}