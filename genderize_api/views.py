from django.shortcuts import render
import requests
from datetime import datetime, timezone
from django.http import JsonResponse
from datetime import datetime, timezone
from rest_framework.response import Response

# Create your views here.
GENDERIZE_API_URL = 'https://api.genderize.io'

def error_response(message, status):
    resp = JsonResponse({'status': 'error', 'message': message}, status=status)
    resp['ACCESS-CONTROL-ALLOW-ORIGIN'] = '*'
    return resp

def task0(request):
    name = request.GET.get('name')

    # Error handling for name parameter
    if not name:
        return error_response('Bad Request', 400)
    
    if not isinstance(name, str):
        return error_response('Unprocessable Entity', 422)

    try:
        response = requests.get(GENDERIZE_API_URL, params={"name": name}, timeout=5)
        response.raise_for_status()
        raw = response.json()
    except requests.exceptions.Timeout:
        return error_response("Genderize API timed out.", 502)
    except requests.exceptions.HTTPError as exc:
        return error_response(
            f"Genderize API returned an error: {exc.response.status_code}", 502
        )
    except requests.exceptions.RequestException as exc:
        return error_response(f"Could not reach Genderize API: {exc}", 502)
    except ValueError:
        return error_response("Genderize API returned an unreadable response.", 502)

    # Extracting gender, probability and count from the API
    gender = raw.get('gender')
    probability = raw.get('probability')
    sample_size = raw.get('count')

    # Genderize edge cases
    if gender is None or sample_size == 0:
        return error_response('No prediction available for the provided name', 500)

    is_confident = bool(
        isinstance(probability, (int, float))
        and probability >= 0.7
        and isinstance(sample_size, int)
        and sample_size >= 100
    )

    
    processed_at = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

    payload = {
        'status': 'success',
        'data': {
            'name': raw.get('name', name),
            'gender': gender,
            'probability': probability,
            'sample_size': sample_size,
            'is_confident': is_confident,
            'processed_at': processed_at
        },
    }

    resp = JsonResponse(payload)
    resp['ACCESS-CONTROL-ALLOW-ORIGIN'] = '*'
    return resp