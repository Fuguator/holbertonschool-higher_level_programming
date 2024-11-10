import os

def generate_invitations(template, attendees):
    if not template or not attendees:
        print('error: not found')
        return
    
    if not isinstance(template, str) or not isinstance(attendees, list):
        print('error: invalid type')
        return
    
    if not all(isinstance(item, dict) for item in attendees):
        print('error: invalid type')
        return
    
    for index, attendee in enumerate(attendees, start=1):
        template_schema = template
        for key in ['name', 'event_title', 'event_date', 'event_location']:
            placeholder = '{' + f'{key}' + '}'
            value = attendee.get(key) or "N/A"
            template_schema = template_schema.replace(placeholder, value)
        if not os.path.exists(f'output_{index}.txt'):
            with open(f'output_{index}.txt', 'w') as file:
                file.write(template_schema)
        else:
            print('error: already exists')
    
if __name__ == "__main__":
    
    attendees = [
    {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
]
    
    with open('template.txt', 'r') as file:
        template_content = file.read()
        
    generate_invitations(template_content, attendees)
