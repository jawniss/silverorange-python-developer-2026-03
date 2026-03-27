from django.db import models  # noqa: F401


class Authors(models.Model):
    # I get errors with models.UUIDField as when Django searched for the post UUID in the DB, it would stop at the first hyphen on the search.
    # Ex: f30b0c7f-e615-4917-98fe-f4f90d74fffc
    # Django stops at the first hyphen and searches for: f30b0c7f
    # Returns no post, as it doesn't match any
    # The workaround I used is using a CharField instead of UUIDField. I could likely use the UUIDField if I stored the UUIDs in the table without the hyphens, or converted them to blobs, but I wanted to store the data exactly as is from the JSONs
    id = models.CharField(primary_key=True, max_length=36, editable=False)
    # Size 255 seems excessive, but rather that than run into too long name errors for now
    full_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    # Without this, Django looks for table "blog_authors" because of directory chain
    class Meta:
        db_table = "authors"


class Posts(models.Model):
    id = models.CharField(primary_key=True, max_length=36, editable=False)
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    # If building a more complex application: Not sure if all future data entries have been published, so allow it to be nullable
    published_at = models.DateTimeField(null=True, blank=True)
    # Needed to explicitly state db_column="author" because Django kept looking for "author_id"
    author = models.ForeignKey(Authors, on_delete=models.CASCADE, db_column="author")

    # Without this, Django looks for table "blog_posts" because of directory chain
    class Meta:
        db_table = "posts"
