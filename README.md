## Inventory-Tracking-App

#### Description:

This app is an inventory tracking web application. You are able to:
 - Create Inventory Items
 - Edit Inventory Items
 - Delete Inventory Items
 - View a list of Inventory Items
 - Create Warehouses and assign inventory to them

#### How to Use:

1. Go to Replit Link: https://replit.com/@Meggin/Shopify-Project#main.py
2. Click "Run" on replit
3. Send Requests by either of the following:
   - Import postman collection in this repository to send requests from Postman 
   - Send a curl request, example to create and item is provided. Refer to the Sample Requests for addional requests that can me made using curl.

```
curl -d '{"client_name":"Meggin", "item_name": "Sugars", "warehouse_id": "None", "destination": "FL", "date_aquired": "05/22", "delivery_date": "05/23"}' -H 'Content-Type: application/json' https://Shopify-Project.meggin.repl.co/create
```

#### Sample Requests:

To create an item:
  POST: https://Shopify-Project.meggin.repl.co/create
  
      {
         "client_name":"Meggin",
         "item_name": "Sugars",
         "warehouse_id": "None",
         "destination": "FL",
         "date_aquired": "05/22",
         "delivery_date": "05/23"
      }
      
      
      
To edit an item, including assignment of warehouse:
  POST: https://Shopify-Project.meggin.repl.co/edit

      {
          "inventory_id": "4",
         "client_name":"Meggin",
         "item_name": "Hairbrush",
         "warehouse_id": "2",
         "destination": "FL",
         "date_aquired": "05/22",
         "delivery_date": "05/23"
      }
    
    
To create a warehouse:
  POST: https://Shopify-Project.meggin.repl.co/warehouses
  
      {
          "warehouse_name": "NC Triangle",
          "address": "000 Chicken Bridge Road Pittsboro NC 27312",
          "phone": "555-555-5555",
          "capacity": "1000000 Sq Feet",
          "capacity_utilization": "68%"
      }
      
      
To delete an item:
  POST: https://Shopify-Project.meggin.repl.co/delete

      {
          "inventory_id": "1"
      }


To view the list of items:
  GET: https://Shopify-Project.meggin.repl.co/view




#### Technology Stack
   * **Backend:** Python, Flask
   

#### Contact 
Meggin Simon: megginsimon@gmail.com
