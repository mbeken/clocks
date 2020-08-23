**Datamodel:**
1. We will use Bucket pattern & Attribute pattern for storing data in Nosql. 
2. We will save One document/per day /Device 3.Sample json is as below 

`{ 
	"id":22222222222, 
	"doctype":"S1", 
	"dchema":"1.0",
	"deviceid":"X1W23",
	"Date":"08/22/2020",
	"Data":[ 
		{"hour":1,"angle":[2,45],"U":"am" },
		{"hour":6,"angle": [6,55],"U":"pm" } 
	] 
}`
