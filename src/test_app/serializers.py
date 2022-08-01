from rest_framework import serializers

from test_app.models import Person, Group, Subject


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = [
            'id', 'first_name', 'last_name', 'age', 'type', 'social_url', 'status', 'updated_at', 'created_at'
        ]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = [
            'name', 'amount_of_people', 'place_in_the_rating', 'created_at', 'updated_at', 'created_at'
        ]


class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subject
        fields = [
            'name', 'number_of_lessons', 'created_at', 'updated_at', 'created_at',
        ]
