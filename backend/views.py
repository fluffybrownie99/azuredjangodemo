from django.shortcuts import render
from utils import client, dbname, collection_name #for azure cosmos db
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
import json
from bson import ObjectId, json_util
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

#Create a new note in our collection
@csrf_exempt
@require_http_methods(["POST"]) 
def create_new_note(request):
    try:
        # Parse request body to get note data
        note_data = json.loads(request.body)

        # Validate note_data here (e.g., check required fields)

        # Insert the note into the MongoDB collection
        result = collection_name.insert_one(note_data)

        # Return success response
        return JsonResponse({"message": "Note created successfully", "id": str(result.inserted_id)})
    except Exception as e:
        # Handle exceptions
        return HttpResponse(status=500)



@csrf_exempt
def get_all_notes(request):
    try:
        # Fetch all notes
        notes_cursor = collection_name.find()

        # Convert cursor to a list of dictionaries
        notes = list(notes_cursor)

        # Use json_util.dumps to serialize the list of notes
        notes_json = json_util.dumps(notes)

        # Return as HttpResponse because JsonResponse expects a dict, not a JSON string
        return HttpResponse(notes_json, content_type='application/json')
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

        

#Get note by ID
@csrf_exempt
def get_note_by_id(request, note_id):
    try:
        note = collection_name.find_one({'_id': ObjectId(note_id)})
        if note:
            # Convert ObjectId to string
            note['_id'] = str(note['_id'])
            return JsonResponse(note)
        else:
            return JsonResponse({'error': 'Note not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

#Update note
@csrf_exempt
@require_http_methods(["PUT"])
def update_note(request, note_id):
    try:
        # Parse request body for update data
        update_data = json.loads(request.body)

        # Perform the update
        collection_name.update_one({'_id': ObjectId(note_id)}, {'$set': update_data})

        return JsonResponse({'message': 'Note updated successfully'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
        
#Delete note
@csrf_exempt
@require_http_methods(["DELETE"])
def delete_note(request, note_id):
    try:
        result = collection_name.delete_one({'_id': ObjectId(note_id)})
        if result.deleted_count:
            return JsonResponse({'message': 'Note deleted successfully'})
        else:
            return JsonResponse({'error': 'Note not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

"""this lets us use the same url 'notes/' but differentiate between a POST request for creating a note and 
a GET request for getting all notes
"""
@csrf_exempt
def notes_handler(request):
    if request.method == 'POST':
        return create_new_note(request)
    elif request.method == 'GET':
        return get_all_notes(request)
    else:
        return JsonResponse({'error': 'Invalid HTTP method'}, status=405)