import uuid

from django.db import models  # noqa: F401
from django.db.backends.base.base import BaseDatabaseWrapper


# AI helped create this model field for keeping the hyphens in the UUID for accessing post details pages
# I was getting errors with the models.UUIDField as when Django searched for the post UUID in the DB, it would stop at the first hyphen on the search.
# Ex: f30b0c7f-e615-4917-98fe-f4f90d74fffc
# Django searches for: f30b0c7f
# Returns no post, as it doesn't match
# I wanted to keep the data in the JSONs exactly as they are in the JSONs; removing the hyphens before inserting into the DB works, but again, I wanted to insert it all as is
class HyphenatedUUIDField(models.UUIDField):
    def get_db_prep_value(
            self, 
            value: uuid.UUID,
            connection: BaseDatabaseWrapper, 
            prepared: bool=False
        ) -> str:
        if value is None:
            return None
        if isinstance(value, uuid.UUID):
            return str(value)
        return str(uuid.UUID(value))

# Timestamp includes timezone info
# in settings.py > USE_TZ = True
# Wary about default behaviour of "default", looks like here we're taking in the authors JSON as already made UUIDs and timestamps so wary if these would conflict
class Authors(models.Model):
    id = HyphenatedUUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # id = models.CharField(primary_key=True, max_length=36, editable=False)
    # Size 255 seems excessive, but rather that than run into too long name errors for now
    full_name = models.CharField(max_length=255)
    # As above comment, if auto generating the timestamps on creation, keep True. If importing data, may need it as False
    # Unsure if meaning when data entry was created, or when Author became Author
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "authors"


class Posts(models.Model):
    id = HyphenatedUUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # id = models.CharField(primary_key=True, max_length=36, editable=False)
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    # Not sure if all entries have been published, so allow it to be nullable
    published_at = models.DateTimeField(null=True, blank=True)
    # TODO: Not 100% sure of cascade deletion behaviour, double check Django implementation only deletes the Post
    # Needed to add db_column="author" because Django kept looking for "author_id"
    author = models.ForeignKey(
        Authors, 
        on_delete=models.CASCADE,
        db_column="author"
    )

    # Without this, Django looks for table "blog_posts" because of directory chain
    class Meta:
        db_table = "posts"