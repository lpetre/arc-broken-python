import json
import arc

def handler(event, context):
  return {'body': json.dumps(arc.reflect())}