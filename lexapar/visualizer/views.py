from django.shortcuts import render
import json
 
 
def validate_data(data):
    if not isinstance(data, list):
        return False, ["Invalid data format. Expected a list."]
    
    errors = []

    for item in data:
        if not isinstance(item, dict):
            errors.append("Each item must be a dictionary.")
            continue

        if 'type' not in item or 'data' not in item or 'name' not in item:
            errors.append("Each item must contain 'type', 'name', and 'data'.")
            continue

        if item['type'] == 'bar':
            if not (isinstance(item['data'], list) and len(item['data']) == 2):
                errors.append("Bar chart data must be a list of two lists.")
                continue
            
            labels, values = item['data']

            if not (isinstance(labels, list) and isinstance(values, list)):
                errors.append("Labels and values must be lists.")
                continue

            if len(labels) != len(values):
                errors.append("Labels and values must have the same length.")
                continue

        elif item['type'] == 'table':
            if not (isinstance(item['data'], list) and all(isinstance(row, dict) for row in item['data'])):
                errors.append("Table data must be a list of dictionaries.")
                continue
            
            keys = set(item['data'][0].keys())
            for row in item['data']:
                if set(row.keys()) != keys:
                    errors.append("All rows in table data must have the same keys.")
                    break

        else:
            errors.append("Unsupported visualization type.")

    return (False, errors) if errors else (True, "Valid")

def index(request):
    data = []
    errors = []

    if request.method == 'POST':
        json_data = request.POST.get('data_json', '[]')

        try:
            parsed_data = json.loads(json_data)
            is_valid, errors = validate_data(parsed_data)
            if is_valid:
                data = parsed_data
        except json.JSONDecodeError:
            errors.append("Invalid JSON format.")
    
    return render(request, 'visualizer/index.html', {
        'data_json': json.dumps(data),   
        'errors': errors
    })
