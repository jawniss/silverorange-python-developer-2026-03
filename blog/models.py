from django.db import models  # noqa: F401
import uuid

# Create your models here.
"""
Authors JSON structure: 
{
    id: UUID, 
    full_name: str,
    created_at: timestamp,
    modified_at: timestamp
}
Would want the created and modified ats to be converted to timestamps
"""

# Looks like django models is like a dict object

# Timestamp includes timezone info
# in settings.py > USE_TZ = True
# Wary about default behaviour of "default", looks like here we're taking in the authors JSON as already made UUIDs and timestamps so wary if these would conflict
class Authors(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Size 255 seems excessive, but rather that than run into too long name errors for now
    full_name = models.CharField(max_length=255)
    # As above comment, if auto generating the timestamps on creation, keep True. If importing data, may need it as False
    # Unsure if meaning when data entry was created, or when Author became Author
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Posts(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    # Not sure if all entries have been published, so allow it to be nullable
    published_at = models.DateTimeField(null=True, blank=True)
    # TODO: Not 100% sure of cascade deletion behaviour, double check Django implementation only deletes the Post
    author = models.ForeignKey(Authors, on_delete=models.CASCADE)