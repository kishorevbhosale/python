from openstack import connection

def auth():
    con = connection.Connection(auth_url="http://10.136.60.28:5000/v2.0",
                                    project_name="admin", username="admin", password="secret")
    return con