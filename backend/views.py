from django.shortcuts import render
from utils import client, dbname, collection_name #for azure cosmos db
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
import json
from bson import ObjectId
# Create your views here.

#Create a new note in our collection
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

# Get all notes
def get_all_notes(request):
    try:
        notes = list(collection_name.find())
        return JsonResponse(notes, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
        

#Get note by ID
def get_note_by_id(request, note_id):
    try:
        note = collection_name.find_one({'_id': ObjectId(note_id)})
        if note:
            return JsonResponse(note)
        else:
            return JsonResponse({'error': 'Note not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

#Update note
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
def notes_handler(request):
    if request.method == 'POST':
        return create_new_note(request)
    elif request.method == 'GET':
        return get_all_notes(request)
    else:
        return JsonResponse({'error': 'Invalid HTTP method'}, status=405)