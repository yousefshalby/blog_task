from rest_framework import serializers
from rest_framework.exceptions import ValidationError



def reshape_error_message(error):
    try:
        error_messages = []
        counter = 0
        for err in error:
            error_messages.append(err + ": ")
            for serr in error[err]:
                error_messages[counter] += serr
            counter += 1
        return error_messages
    except Exception:
        pass


class CustomModelSerializer(serializers.ModelSerializer):
    def is_valid(self, raise_exception=False):
        try:
            is_valid = super(CustomModelSerializer, self).is_valid(raise_exception)
            self._errors = reshape_error_message(self._errors)
            return is_valid
        except ValidationError as e:
            e.detail = {"details": reshape_error_message(e.detail)}
            raise e
