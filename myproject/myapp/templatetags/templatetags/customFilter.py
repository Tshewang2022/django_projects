from django import template
register=template.Library()

@register.filter(name='addTitle')

def addTitle(name,gender):
    if gender.lower()=='male':
        return f'Mr. {name}'
    elif gender.lower()=='female':
        return f'Ms. {name}'
    else:
        return name