from django.db.models import Model, CharField, IntegerField, DateTimeField, BooleanField


class DateTimeMixin(Model):
    created_at = DateTimeField(auto_now_add=True, null=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Person(DateTimeMixin, Model):
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    age = IntegerField()
    type_of_person = CharField(max_length=30)
    status = BooleanField()


class Group(DateTimeMixin, Model):
    amount_of_people = IntegerField()
    place_in_the_rating = IntegerField(null=True)


class Subject(DateTimeMixin, Model):
    subject_name = CharField(max_length=50)
    number_of_lessons = IntegerField()


class Course(DateTimeMixin, Model):
    course_name = CharField(max_length=50)
    difficulty = CharField(max_length=50)
    number_of_groups = IntegerField()


class Lesson(DateTimeMixin, Model):
    topic = CharField(max_length=50)
    duration = IntegerField()
    difficulty = CharField(max_length=50)
