from django import template
from crum import get_current_user
from company_app.models import Company
from admin_app.models import Resume


register = template.Library()


@register.inclusion_tag('drop_down_menu.html')
def show_drop_down_menu():
    try:
        company = Company.objects.get(owner=get_current_user())
    except Company.DoesNotExist:
        company = None
    try:
        resume = Resume.objects.get(user=get_current_user())
    except Resume.DoesNotExist:
        resume = None
    return {'company': company,
            'resume': resume}





