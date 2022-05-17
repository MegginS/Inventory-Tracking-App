from flask import (Flask, flash, session, redirect, make_response, request, jsonify)
import json

app = Flask(__name__)


class Item():
    """An item."""

    def __init__(self, inventory_id, client_name, item_name, warehouse_id, destination, date_aquired, delivery_date):
      self.inventory_id = inventory_id
      self.client_name= client_name
      self.item_name= item_name
      self.warehouse_id= warehouse_id
      self.destination= destination
      self.date_aquired= date_aquired
      self.delivery_date= delivery_date

class Warehouse():
  """A Warehouse"""

  def __init__(self, warehouse_id, warehouse_name, address, phone, capacity, capacity_utilization):
    self.warehouse_id = warehouse_id
    self.warehouse_name= warehouse_name
    self.address= address
    self.phone= phone
    self.capacity = capacity
    self.capacity_utilization = capacity_utilization


def verify_attributes(attr1, attr2, attr3, mydict):

    if set((attr1, attr2, attr3)).issubset(mydict.keys()):
       return True
    else:
        return False

def attribute_values(attr_list):

    for attr in attr_list:
        if len(attr) <= 2:
            return False
    return True
        

items = []

@app.route('/create', methods = ['POST'])
def creation():


    if len(items) == 0:
        item_id = 1
    else:
        item_id = items[-1].inventory_id + 1

    item_details= request.get_json()

    attribute_check = verify_attributes("client_name", "item_name", "date_aquired", item_details)
    if attribute_check is False:
        response = {"Status": "Failed", "Error": "Missing Required Attribute"}
        return jsonify(response)


    inventory_id= item_id
    client_name= item_details["client_name"]
    item_name= item_details["item_name"]
    warehouse_id= item_details["warehouse_id"] if "warehouse_id" in item_details else None
    destination= item_details["destination"] if "destination" in item_details else None
    date_aquired= item_details["date_aquired"]
    delivery_date= item_details["delivery_date"] if "delivery_date" in item_details else None

    value = attribute_values([client_name, item_name, date_aquired])
    if value is False:
        response = {"Status": "Failed", "Error": "Required attributes must be minimum 2 characters"}
        return jsonify(response)


    item = Item(inventory_id= inventory_id, client_name= client_name, item_name= item_name, warehouse_id= warehouse_id, destination= destination, date_aquired= date_aquired, delivery_date= delivery_date)

    
    items.append(item)

    response = {"Status": "Success!", "Created": item_name, "Inventory_Id": inventory_id}
    return jsonify(response)


warehouses = []

@app.route('/warehouses', methods = ['POST'])
def create_warehouses():
    """Create Warehouses"""

    if len(warehouses) == 0:
        wh_id = 1
    else:
        wh_id = warehouses[-1].warehouse_id + 1

    warehouse_details= request.get_json()

    attribute_check = verify_attributes("warehouse_name", "address", "phone", warehouse_details)
    if attribute_check is False:
        response = {"Status": "Failed", "Error": "Missing Required Attribute"}
        return jsonify(response)

    warehouse_id= wh_id
    warehouse_name= warehouse_details["warehouse_name"]
    address= warehouse_details["address"]
    phone= warehouse_details["phone"]
    capacity= warehouse_details["capacity"] if "capacity" in warehouse_details else None
    capacity_utilization= warehouse_details["capacity_utilization"] if "capacity_utilization" in warehouse_details else None

    value = attribute_values([warehouse_name, address, phone])
    if value is False:
        response = {"Status": "Failed", "Error": "Required attributes must be minimum 2 characters"}
        return jsonify(response)


    warehouse = Warehouse(warehouse_id= warehouse_id, warehouse_name= warehouse_name, address= address, phone= phone, capacity=capacity, capacity_utilization= capacity_utilization)
  
    warehouses.append(warehouse)

    response = {"Status": "Success!", "Created": warehouse_name, "Warehouse_Id": warehouse_id}
    return jsonify(response)


@app.route('/edit', methods = ['POST'])
def edit():
    """Edit Items, Assign to Warehouse"""

    edit_request= request.get_json()
    inventory_id= edit_request["inventory_id"]

    if len(items) == 0:
        response = {"Status": "Failed", "Error": "Inventory_ID non existant"}
        return jsonify(response)

    for item in items:

        if item.inventory_id == int(inventory_id):
            item.client_name= edit_request["client_name"]
            item.item_name= edit_request["item_name"]
            item.warehouse_id= edit_request["warehouse_id"]
            item.destination= edit_request["destination"]
            item.date_aquired= edit_request["date_aquired"]
            item.delivery_date= edit_request["delivery_date"]

            response = {"Status": "Success!", "Edited item": inventory_id, "client_name": item.client_name, "item_name": item.item_name, "warehouse_id": item.warehouse_id, "destination": item.destination, "date_aquired": item.date_aquired, "delivery_date": item.delivery_date}
            return jsonify(response)

    response = {"Status": "Failed", "Inventory_Id": inventory_id, "Error": "Inventory_ID non existant"}
    return jsonify(response)



@app.route('/delete', methods = ['POST'])
def delete():
    """Delete Items"""

    delete_request= request.get_json()
    inventory_id= delete_request["inventory_id"]
    
    if len(items) == 0:
        response = {"Status": "Failed", "Error": "Inventory_ID non existant"}
        return jsonify(response)

    for item in items:

        if item.inventory_id == int(inventory_id):
            deleted_item = item
            item_name = item.item_name
            items.remove(deleted_item)
            response = {"Status": "Success!", "Deleted": item_name, "Inventory_Id": inventory_id}
            return jsonify(response)

    response = {"Status": "Failed", "Inventory_Id": inventory_id, "Error": "Inventory_ID non existant"}
    return jsonify(response)



@app.route('/view')
def view():
    """View" Items"""

    response = {"Status": "Success!", "Data": []}

    for item in items:
        response["Data"].append({"inventory_id": item.inventory_id, "client_name": item.client_name, "item_name": item.item_name, "warehouse_id": item.warehouse_id, "destination": item.destination, "date_aquired": item.date_aquired, "delivery_date": item.delivery_date})

    return jsonify(response)


@app.route('/')
def home():
    return ('Welcome to my Logistics App, here is a link to the Github README')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)