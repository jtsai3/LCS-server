from rest_framework import serializers

class SetOfStringSerializer(serializers.Serializer):
    setOfStrings = serializers.ListSerializer(
        child=serializers.DictField(
            child=serializers.CharField(required=True)
        )
    )

    def validate_setOfStrings(self, value):
        # check if setOfStrings is empty
        if not value:
            raise serializers.ValidationError("setOfStrings should not be empty")
        # check that keys are 'value'
        try:
            values = [v["value"] for v in value]
        except KeyError:
            raise serializers.ValidationError("setOfStrings must be a list of dictionaries with key 'value'")
        # check if setOfStrings is a set
        if len(set(values)) != len(values):
            raise serializers.ValidationError("setOfStrings must be a Set")
        return value