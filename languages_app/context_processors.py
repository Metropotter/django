from .models import SiteVisitor

def visitor_count(request):
    """Add total_visitors to all templates"""
    try:
        visitor_counter = SiteVisitor.get_visitor_count()
        return {
            'total_visitors': visitor_counter.total_visitors
        }
    except:
        return {'total_visitors': 0}