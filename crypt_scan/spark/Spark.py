class Spark():

    columns = [
        "asset",
        "exchange",
        "side",
        "price",
        "size",
        "timestamp",
    ]

    __init__(self, schema: StructType = StructType([])):
        self.spark = SparkSession
            .builder
            .appName("Broker Order Book Cache")
            .getOrCreate()

        self.df = self.spark.createDataFrame([], self.columns)

    loadJsonToDataFrame(self, data: Dict):
        # Take in json file containing last 5 seconds entries
        data = list((x for x in data.values())
        newRow = self.spark.createDataFrame(data, self.columns)
        df = spark.read.format('org.apache.spark.sql.json').load("resources/order_book.json")
        self.df = df.union(newRow)
