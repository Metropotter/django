from django.db import models

class Language(models.Model):
    APPLICATION_AREAS = [
        ('web', 'Web Development'),
        ('mobile', 'Mobile Development'),
        ('desktop', 'Desktop Applications'),
        ('data_science', 'Data Science & AI'),
        ('systems', 'Systems Programming'),
        ('game', 'Game Development'),
        ('embedded', 'Embedded Systems'),
    ]
    
    name = models.CharField(max_length=100, unique=True)
    logo = models.ImageField(upload_to='language_logos/', blank=True, null=True)
    description = models.TextField()
    year_created = models.IntegerField()
    main_application_area = models.CharField(max_length=50, choices=APPLICATION_AREAS)
    view_count = models.IntegerField(default=0)  # ← Make sure this line exists
    last_viewed = models.DateTimeField(auto_now=True)  # ← And this line exists
    
    def __str__(self):
        return self.name
    
    def increment_view_count(self):
        self.view_count += 1
        self.save()
    
    class Meta:
        ordering = ['name']