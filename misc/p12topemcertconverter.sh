# Script for converting from "p12" certificate to "pem" certificate
# Require openssl
#
# Usaga:
#
#
# p12topemcertconverter "p12 cert file"
echo "##### Convert $1 to apns-dev-cert.pem #####"
openssl pkcs12 -in $1 -out apns-dev-cert.pem -nodes -clcerts 
echo "##### Done #####"