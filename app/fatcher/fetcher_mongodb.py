import pymongo
from fetcher_abc import FetcherABC

class FetcherMongoDB(FetcherABC):

    def open_connection(self):
        try:
            self.my_client = pymongo.MongoClient(self.connection_string)
        except Exception as e:
            raise RuntimeError("Failed to connect to MongoDB") from e

    def close_connection(self):
        if self.my_client:
            self.my_client.close()

    def get_database_names(self):
        return self.my_client.list_database_names()

    def get_dataset_names(self):
        return self.my_client.list_collection_names()


    def get_field_names(self, db_name, col_name):
        col = self.my_client[db_name][col_name]

        pipeline = [
            {"$project": {"fields": {"$objectToArray": "$$ROOT"}}},
            {"$unwind": "$fields"},
            {"$group": {"_id": None, "all_fields": {"$addToSet": "$fields.k"}}}
        ]

        result = list(col.aggregate(pipeline))
        return result[0]["all_fields"] if result else []


    def get_collection_data(self, db_name, col_name):
        col = self.my_client[db_name][col_name]
        return col.find()