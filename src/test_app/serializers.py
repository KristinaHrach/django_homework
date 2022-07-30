from rest_framework import serializers

from test_app.models import Person, Group, Subject


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = [
            'id', 'first_name', 'last_name', 'age', 'type', 'social_url', 'status'
        ]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = [
            'amount_of_people', 'place_in_the_rating'
        ]


class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subject
        fields = [
            'name', 'number_of_lessons'
        ]
