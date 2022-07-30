from django.db.models import Model, CharField, IntegerField, DateTimeField, BooleanField, \
    URLField, ForeignKey, CASCADE, OneToOneField

from test_app.choices import TypeChoices


class DateTimeMixin(Model):
    created_at = DateTimeField(auto_now_add=True, null=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Person(DateTimeMixin, Model):
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    age = IntegerField()
    type = CharField(max_length=30, choices=TypeChoices.choices)
    social_url = URLField(max_length=500, null=True)
    status = BooleanField(default=True)

    group = ForeignKey('Group', on_delete=CASCADE, null=True)
    course = ForeignKey('Course', on_delete=CASCADE, null=True)


class Group(DateTimeMixin, Model):
    amount_of_people = IntegerField()
    place_in_the_rating = IntegerField(null=True)


class Subject(DateTimeMixin, Model):
    name = CharField(max_length=50)
    number_of_lessons = IntegerField()

    lesson = ForeignKey('Lesson', on_delete=CASCADE, null=True)


class Course(DateTimeMixin, Model):
    name = CharField(max_length=50)
    difficulty = CharField(max_length=50)
    number_of_groups = IntegerField()

    group = OneToOneField(Group, on_delete=CASCADE, null=True)
    subject = ForeignKey(Subject, on_delete=CASCADE, null=True)


class Lesson(DateTimeMixin, Model):
    topic = CharField(max_length=50)
    duration = IntegerField()
    difficulty = CharField(max_length=50)
