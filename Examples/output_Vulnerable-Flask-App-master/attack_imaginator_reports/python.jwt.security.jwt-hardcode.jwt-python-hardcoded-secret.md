
# Attack Imaginator Report

Hi dear security enthusiast! (^^,)
I'm your fellow attack imaginator. I'll provide possible hacking scenarios over your code review findings.
Hope, they'll help you to test your systems and increase their security bar! 
Don't forget, I don't accept any responsibility in your actions.
Please examine the scenarios that I'll create properly for not causing any harm to your test scope.


## CODE REVIEW FINDING DETAILS:

**FINDING TITLE:**  

python.jwt.security.jwt-hardcode.jwt-python-hardcoded-secret

### FINDING SEVERITY:

MEDIUM

### FINDING EXPLANATION:

Hardcoded JWT secret or private key is used. This is a Insufficiently Protected Credentials weakness: https://cwe.mitre.org/data/definitions/522.html Consider using an appropriate security mechanism to protect the credentials (e.g. keeping secrets in environment variables)

### VULNERABLE CODE PATH:

```
/Users/USERNAME/Downloads/Vulnerable-Flask-App-master/app/app.py
```

### VULNERABLE CODE SNIPPET:

```
            auth_token = jwt.encode({'user': username, 'exp': get_exp_date(), 'nbf': datetime.datetime.utcnow(), 'iss': 'we45', 'iat': datetime.datetime.utcnow()}, app.config['SECRET_KEY_HMAC'], algorithm='HS256')
```

## ATTACK SCENARIO DETAILS:


### Impact

- Critical

### Explanation

The hardcoded secret key 'we45' in the JWT token is a significant security risk, as it allows an attacker to easily obtain the decryption key and potentially access sensitive data. Hardcoding credentials directly into the source code is a common mistake that can be exploited by attackers.

                        In this scenario, an attacker could intercept the JWT token or gain access to the server's logs to obtain the value of 'we45'. Once in possession of the secret key, the attacker could use it to decrypt sensitive data, such as user credentials or encryption keys.

### Steps to Reproduce

1. **Obtain the JWT token**: The attacker would need to obtain the JWT token sent by the server. This can be done through various means, such as sniffing the network traffic or gaining access to the server's logs.
                        
                        2. **Extract the secret key**: The attacker would then need to extract the value of 'we45' from the JWT token. This could be done using a decryption tool or by analyzing the token's header.

                        3. **Use the secret key for decryption**: Once the secret key is obtained, the attacker could use it to decrypt the sensitive data stored on the server.

### Proof of Concept (PoC)

```python
import jwt

# Decryption function using the hardcoded secret key
def decrypt_token(token):
    secret_key = 'we45'
    try:
        payload = jwt.decode(token, secret_key, algorithms=['HS256'])
        return payload['user']
    except jwt.ExpiredSignatureError:
        print("Token has expired")
    except jwt.InvalidTokenError:
        print("Invalid token")

# Example usage
token = "your_jwt_token_here"
decrypted_username = decrypt_token(token)
print(decrypted_username)
                        ```
