class VisitorCounterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        # Increment visitor count for each request
        from .models import SiteVisitor
        visitor_counter = SiteVisitor.get_visitor_count()
        visitor_counter.increment_visitors()
        
        response = self.get_response(request)
        return response