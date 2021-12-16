# SSL Checker - AWS Lambda Funtion

----SSLChecker AWS lambda function-----

The Purpose of this tool is to check the status of SSL expiration for a list of domains.
list of domains can be provided and placed into an S3 bucket, and referenced in this function.

The function is apart of an AWS Cloud Formation Stack- this function would be invokded by an AWS API Gateway via a GET response.

The lambda function will retrieve the list of domains and then iterate through it to check if the SSL is valid, retrieve the exipration date, and then provide warning if exiration is coming up within a 2 week period based off of the "notAfter" date retrieved via certificate details for the domain.

The logs can then be stored into an S3 bucket, and an SNS notifcication topic can be set up to send alerts based on status

Chron job can then be added to invoke the application at a given time interval.

AWS Code pipeline is set up for CI/CD build and deployment with this github repo so that in the event that any packages need to be updates, modifications etc, they can be updated with the "change" action

-------- the current Application will only check for google.com-----

EXAMPLE of Response from invocation:

---

Response
[
{
"success": true,
"cert_status": "OK",
"domain": "google.com"
}
]

Function Logs
START RequestId: 89ad60aa-234e-4a91-b083-e6c6518af887 Version: $LATEST
SSL cert for %s expires at %s google.com 2022-02-21T02:22:32
SSL certificate doesn't expire for a while - you're set!
END RequestId: 89ad60aa-234e-4a91-b083-e6c6518af887
REPORT RequestId: 89ad60aa-234e-4a91-b083-e6c6518af887 Duration: 295.70 ms Billed Duration: 296 ms Memory Size: 128 MB Max Memory Used: 55 MB Init Duration: 242.37 ms

---

TEST
invokation URL: https://ozltfq4jrf.execute-api.us-east-2.amazonaws.com/testsandbox/
