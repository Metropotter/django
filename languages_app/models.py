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

class SiteVisitor(models.Model):
    total_visitors = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Total Visitors: {self.total_visitors}"
    
    def increment_visitors(self, request):  # FIX: Add 'self' as first parameter
        """Count only once per session"""
        if not request.session.get('has_been_counted'):
            self.total_visitors += 1
            self.save()
            request.session['has_been_counted'] = True
    
    @classmethod
    def get_visitor_count(cls):
        """Get or create the singleton visitor counter"""
        obj, created = cls.objects.get_or_create(id=1)
        return obj