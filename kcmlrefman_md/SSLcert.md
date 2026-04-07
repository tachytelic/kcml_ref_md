# SSL Certificates

> Reference for generating and deploying X.509 SSL certificates for KCML servers.

## Description

KCML SSL servers require an X.509 server certificate. Certificates have a public component and an encrypted private key (protected by a passphrase).

### Certificate formats

| Format | Description |
|--------|-------------|
| PEM | Base64 text between `-----BEGIN...-----` markers (OpenSSL default) |
| DER | Binary format (Java) |
| PKCS12 | Microsoft format |

KCML uses PEM format.

## Using a public CA

For internet-facing servers, purchase a signed certificate from a public CA (DigiCert, Comodo, etc.). Their public keys are already trusted by browsers and OS SSL libraries.

1. Generate a certificate request with OpenSSL.
2. Submit to the CA.
3. Deploy the signed certificate.

Note: certificates expire (typically annually) and must be renewed.

## Self-signed certificates (for internal use)

For internal KCML-to-KCML connections, generate a self-signed CA and server certificate using OpenSSL:

```sh
# 1. Generate CA root certificate
openssl req -newkey rsa:1024 -sha1 -keyout rootkey.pem -out rootreq.pem
openssl x509 -req -in rootreq.pem -signkey rootkey.pem -out rootcert.pem
cat rootcert.pem rootkey.pem > root.pem

# 2. Generate server certificate (signed by CA)
openssl req -newkey rsa:1024 -sha1 -keyout serverkey.pem -out serverreq.pem
openssl x509 -req -in serverreq.pem -CA root.pem -CAkey root.pem \
  -CAcreateserial -out servercert.pem
cat servercert.pem serverkey.pem rootcert.pem > server.pem
```

The `server.pem` file contains the server certificate, private key, and CA chain.

## Notes

- OpenSSL is included in most Linux distributions; also available at openssl.org.
- The private key passphrase must be entered when starting an SSL server.
- Clients connecting to a self-signed server may warn about certificate authenticity but the connection is still encrypted.

## See Also

- `SSL` — working with secure sockets in KCML
- `SystemRequirements` — platform SSL support matrix
