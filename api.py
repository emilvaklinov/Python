from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

# validate the code 
data = {
	"data": {
		"profile": {
			"id": "0e1834fcb6cc7a9060847e1f053cf078",
			"phone": "+4470000000000",
			"appId": "B013A3ED-D957-4FB3-8055-0671E682B8E6",
			"verified": True,
			"active": True,
			"groups": [
				{
					"id": "9f17582431820a532f44f4f3fc3a58e7",
					"source": "group",
					"name": "Shopping",
					"credentials": [
						{
							"id": "a901e5f80d65125051f7fb2246654280",
							"note": "A note about this account",
							"groupId": "9f17582431820a532f44f4f3fc3a58e7",
							"name": "Amazon",
							"username": "username1",
							"email": "email1",
							"password": "password1",
                            "logo": "https://logo.clearbit.com/amazon.com"
						}
					]
				},
				{
					"id": "3a5e14968c33fdaa0fc8cecbf5f6cce8",
					"source": "group",
					"name": "Lifestyle",
					"credentials": [
						{
							"id": "294735b9cf243d5accb9cf4c27f6acd0",
							"note": "A note about this account",
							"groupId": "3a5e14968c33fdaa0fc8cecbf5f6cce8",
							"name": "Fitbit",
							"username": "username2",
							"email": "email2",
							"password": "password2",
                            "logo": "https://logo.clearbit.com/fitbit.com"
						}
					]
				},
				{
					"id": "a35cfa8fae417dcaa33bb09a00843663",
					"source": "group",
					"name": "Travel",
					"credentials": [
						{
							"id": "c2aacc3583bf7fe849ce58d1903e56bb",
							"note": "A note about this account",
							"groupId": "a35cfa8fae417dcaa33bb09a00843663",
							"name": "Booking.com",
							"username": "username3",
							"email": "email3",
							"password": "password3",
                            "logo": "https://logo.clearbit.com/booking.com"
						},
						{
							"id": "bb5c79bee8b46e146c92f645b619a6f3",
							"note": "A note about this account",
							"groupId": "a35cfa8fae417dcaa33bb09a00843663",
							"name": "Airbnb",
							"username": "username4",
							"email": "email4",
							"password": "password4",
                            "logo": "https://logo.clearbit.com/airbnb.com",
							"dashboardSpaceId": None,
							"phone": "",
							"publicKey": "5pA182ih6drYyk5Bri/MrdVoCWwiJL6M2coqo7eBhkfCNzhlwtf5xnOX61ixTaY42Ta7aUVmCrU/eb6E9PVi6GWTEbTsuswa+PsLjOIzxLJvjnWRnnYacubnI/E=",
							"secretKey": "L37v19Yl10R71RgDeYrUNQcxXI/hHxikp3GOMo26yjI7MpN79SEF4ilQ/1b74Rp1bClOCavEhEF9MHvxCP3hTKI9NMrL01vveLOkA5NW+sOGgKV6URMMci2ndqc=",
							"shared": False
						}
					]
				}
			]
		}
	}
}

class DataList(Resource):
  def get(self):
    return data

api.add_resource(DataList, '/data')
# @app.route("/data", methods=["GET"])
# def get_data():
    # return jsonify(data)



if __name__ == "__main__":
  app.run(debug=True)
# if __name__ == '__main__':
#   app.run(host='0.0.0.0', port=30007, debug=True)