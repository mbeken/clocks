import json
import re

from flask import Response
import uuid

from google.cloud import datastore


class Helpers:
    STATUS_OK = 200
    STATUS_BAD_REQUEST = 400
    STATUS_SERVER_ERROR = 500

    @staticmethod
    def standard_response(status, payload):
        json_data = json.dumps({
            'response': payload
        }, sort_keys=True, indent=4, separators=(',', ': '))
        resp = Response(json_data, status=status, mimetype='application/json')
        return resp

    @staticmethod
    def success(payload):
        return Helpers.standard_response(Helpers.STATUS_OK, payload)

    @staticmethod
    def error(status, error_info):
        return Helpers.standard_response(status, {
            'error': error_info
        })

    @staticmethod
    def bad_request(error_info):
        return Helpers.error(Helpers.STATUS_BAD_REQUEST, error_info)

    @staticmethod
    def validate_and_parse_input(time: str):
        """
        Validates user input.

        For an input to be valid, string should contain at least 3 characters
        and the all characters except ':' should be digits
        """
        if time is None or not re.match(r'^\d{1,2}:\d{1,2}$', time):
            return False
        hour, minute = map(int, time.split(r':'))
        if type(hour) != int or type(minute) != int:
            return False

        if 0 <= hour < 24 and 0 <= minute < 60:
            hour = hour % 12
            minute = minute
            return hour, minute
        else:
            return False


class DatastoreClient:
    def __init__(self, kind):
        self.client = datastore.Client(project='ci-cd-clock-angles', namespace='default')
        self.kind = kind

    def log_to_datastore(self, request_time, response_angle):
        name = str(uuid.uuid4())
        log_key = self.client.key(self.kind, name)

        log_entry = datastore.Entity(key=log_key)
        log_entry['time'] = request_time
        log_entry['response'] = response_angle

        # Saves the entity
        self.client.put(log_entry)
