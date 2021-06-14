import json

def response(result, message = ''):
	return json.dumps({"success": result, "message": message})

