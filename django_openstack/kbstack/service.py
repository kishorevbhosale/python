
from . import credential

con = credential.auth()
###############################################################################################

def list_servers():
    print("List Servers:")
    server = list()
    for s in con.compute.servers():
        #server.append({"id": s.id, "name" : s.name})
        server.append(s)
    return server

###############################################################################################

def list_images():
    print("List Images:")
    image = list()
    for i in con.image.images():
        image.append(i)
    return image

###############################################################################################

def list_flavors():
    print("List Flavors:")
    flavor = list()
    for f in con.compute.flavors():
        flavor.append(f)
    return flavor

###############################################################################################

def list_networks():
    print("List Networks:")
    network = list()
    for n in con.network.networks():
        network.append(n)
    return network

###############################################################################################

def create_server(instance_name, image_name, flavor_name):

    instance = instance_name
    image = image_name
    flavor = flavor_name

    server = con.compute.create_server(name=instance, image_id=image, flavor_id=flavor)

    print server
    return server

###############################################################################################
def delete_server(instance_name):
    instance = instance_name

    server = con.compute.find_server(instance)
    con.compute.delete_server(server)
