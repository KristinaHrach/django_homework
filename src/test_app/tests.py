from django.urls import reverse
from rest_framework.test import APITestCase

from test_app.models import Person, Group, Subject


class PersonViewTestCase(APITestCase):

    def setUp(self):
        self.person = Person.objects.create(
            first_name='test_first_name', last_name='test_last_name', age=10, type='test_type'
        )

    def test_person_get(self):
        response = self.client.get(reverse('person-list'))

        self.assertDictEqual(response.json(),
                             {
                                 "count": 1,
                                 "next": None,
                                 "previous": None,
                                 "results": [
                                     {
                                         "id": 1,
                                         "first_name": "test_first_name",
                                         "last_name": "test_last_name",
                                         "age": 10,
                                         "type": "test_type",
                                         "social_url": None,
                                         "status": True,

                                     },
                                 ]
                             }
                             )

    def test_create_person(self):
        self.client.post(
            reverse('person-list'),
            data={
                'first_name': 'New',
                'last_name': 'Person',
                'age': 12,
                'type': 'S'
            }
        )
        self.assertEqual(Person.objects.count(), 2)

    def test_delete_person(self):
        self.client.delete(
            reverse('person-detail',
                    kwargs={'pk': self.person.pk})
        )
        self.assertEqual(
            Person.objects.count(), 0
        )

    def test_update_person(self):
        self.client.put(
            reverse('person-detail', kwargs={'pk': self.person.pk}),
            data={
                'first_name': 'Updated',
                'last_name': 'Person',
                'age': 13,
                'type': 'S',
            })
        person = Person.objects.first()

        self.assertEqual(person.type,
                         'S', )


class GroupViewTestCase(APITestCase):
    def setUp(self):
        self.group = Group.objects.create(
            name='test_group', amount_of_people=12, place_in_the_rating=2
        )

    def test_group_get(self):
        response = self.client.get(reverse('group-list'))

        self.assertDictEqual(response.json(),
                             {
                                 "count": 1,
                                 "next": None,
                                 "previous": None,
                                 "results": [
                                     {
                                         "name": "test_group",
                                         "amount_of_people": 12,
                                         "place_in_the_rating": 2
                                     },
                                 ]
                             })

    def test_create_group(self):
        self.client.post(
            reverse('group-list'),
            data={
                "name": "new_group",
                "amount_of_people": 10,
                "place_in_the_rating": 1
            }
        )
        self.assertEqual(Group.objects.count(), 2)

    def test_delete_group(self):
        self.client.delete(
            reverse('group-detail',
                    kwargs={'pk': self.group.pk})
        )

        self.assertEqual(Group.objects.count(), 0)

    def test_update_group(self):
        self.client.put(
            reverse('group-detail', kwargs={'pk': self.group.pk}),
            data={
                "name": "second_group",
                "amount_of_people": 10,
                "place_in_the_rating": 1
            }
        )
        group = Group.objects.first()

        self.assertEqual(group.name, 'second_group')


class SubjectViewTestCase(APITestCase):
    def setUp(self):
        self.subject = Subject.objects.create(
            name='test_subject', number_of_lessons=22,
        )

    def test_subject_get(self):
        response = self.client.get(reverse('subject-list'))

        self.assertDictEqual(response.json(),
                             {
                                 "count": 1,
                                 "next": None,
                                 "previous": None,
                                 "results": [
                                     {
                                         "name": "test_subject",
                                         "number_of_lessons": 22
                                     }
                                 ]
                             }
                             )

    def test_create_subject(self):
        self.client.post(
            reverse('subject-list'),
            data={
                "name": "new_subject",
                "number_of_lessons": 20
            }
        )
        self.assertEqual(Subject.objects.count(), 2)

    def test_delete_subject(self):
        self.client.delete(
            reverse('subject-detail',
                    kwargs={'pk': self.subject.pk})
        )
        self.assertEqual(
            Subject.objects.count(), 0
        )

    def test_update_subject(self):
        self.client.put(
            reverse('subject-detail', kwargs={'pk': self.subject.pk}),
            data={
                "name": "new_subject",
                "number_of_lessons": 34
            })
        subject = Subject.objects.first()

        self.assertEqual(subject.number_of_lessons, 34)
