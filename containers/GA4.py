from domain.Variable import Variable
from domain.Container import Container
from domain.Trigger import Trigger



def generate_ga4_standard_container(website: str, ga_mess_id: str, pixel_id:str, typ:str):

    container = Container(website)
        
    #var
    ga4_mess_id = Variable("MessID", "c", {"type": "template", "key":"value", "value":{ga_mess_id}})
    meta_pixel_id = Variable("Meta Pixel ID", "c", {"type": "template", "key":"value", "value":{pixel_id}})

    #trigger
    form_thank_you = Trigger("WESEO - Danke Seite", "pageview", [{"type": "contains", "parameter": [
            {
              "type": "template",
              "key": "arg0",
              "value": "{{Page Path}}"
            },
            {
              "type": "template",
              "key": "arg1",
              "value": "thank-you"
            }
          ]}])    

    #tags

    


