# FOR THE OBJECTIFICATION OF ALL DISCRIMINATORY CHARACTERISTICS EVERYWHERE
# sturmback

import base64, pickle

def create_object(object_name, parent=None):
    if not parent:
        parent = {'name': 'object', 'parent': {'name': 'object'}}
    objectifect = {'name': object_name, 'parent': parent}
    return objectifect

def load_object(encoded_state):
    unencode = base64.b64decode(encoded_state)
    return pickle.loads(unencode)

def save_object(object_o):
    unencode = pickle.dumps(object_o)
    return base64.b64encode(unencode)

def set_attrib(object_o, attrib_name, attribute):
    object_o[attrib_name] = attribute

def remove_attrib(object_o, attrib_name):
    del object_o[attrib_name]

def get_attrib(object_o, attrib_name):
    return object_o[attrib_name]

def attrib_list(object_o):
    return object_o.keys()

def print_object(object_o):
    attr = []
    response = "%s(%s)->%s.\n"
    for i in object_o.keys():
        if not i == "name":
            if i == "parent":
                if object_o['name'] != object_o['parent']['name']:
                    response += print_object(object_o['parent'])
            else:
                attr.append((i, object_o[i]))
    response = response % (object_o['name'], ", ".join("%s %s" % (i[0], i[1]) for i in attr), object_o['parent']['name'])
    return response
