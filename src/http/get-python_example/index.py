import json
import arc

def handler(event, context):
  return {'body': json.dump(arc.reflect())}