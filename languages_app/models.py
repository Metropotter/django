from django.db import models
from django.contrib.auth.models import User

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
    
    DIFFICULTY_LEVELS = [
        ('beginner', 'Beginner Friendly'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]
    
    name = models.CharField(max_length=100, unique=True)
    logo = models.ImageField(upload_to='language_logos/', blank=True, null=True)
    description = models.TextField()
    year_created = models.IntegerField()
    main_application_area = models.CharField(max_length=50, choices=APPLICATION_AREAS)
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_LEVELS, default='intermediate')  # ← ADD THIS LINE
    view_count = models.IntegerField(default=0)
    last_viewed = models.DateTimeField(auto_now=True)
    
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

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_verified = models.BooleanField(default=False)
    verification_token = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.user.username

class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.CharField(max_length=100, blank=True, help_text="Comma-separated tags")
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    mentor = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    answered_at = models.DateTimeField(auto_now_add=True)
    is_official_answer = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-answered_at']
    
    def __str__(self):
        return f"Answer to: {self.question.title}"

class Comment(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created_at']
    
    def __str__(self):
        return f"Comment by {self.user.username}"