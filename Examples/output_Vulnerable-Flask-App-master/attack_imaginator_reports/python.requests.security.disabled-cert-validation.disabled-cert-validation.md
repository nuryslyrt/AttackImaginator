
# Attack Imaginator Report

Hi dear security enthusiast! (^^,)
I'm your fellow attack imaginator. I'll provide possible hacking scenarios over your code review findings.
Hope, they'll help you to test your systems and increase their security bar! 
Don't forget, I don't accept any responsibility in your actions.
Please examine the scenarios that I'll create properly for not causing any harm to your test scope.


## CODE REVIEW FINDING DETAILS:

**FINDING TITLE:**  

python.requests.security.disabled-cert-validation.disabled-cert-validation

### FINDING SEVERITY:

LOW

### FINDING EXPLANATION:

Certificate verification has been explicitly disabled. This permits insecure connections to insecure servers. Re-enable certification validation.

### VULNERABLE CODE PATH:

```
/Users/USERNAME/Downloads/Vulnerable-Flask-App-master/tests/e2e_zap.py
```

### VULNERABLE CODE SNIPPET:

```
search_customer_username = requests.post(target_url + '/search', json=search, proxies=proxies, headers=auth_header, verify=False)
```

## ATTACK SCENARIO DETAILS:


### Impact

- Low

### Explanation

The code review finding indicates that certificate verification is disabled for the `requests` library, which allows insecure connections to vulnerable servers. When `verify=False`, the `requests` library will not check the validity of the server's SSL/TLS certificate, making it easier for an attacker to intercept or tamper with sensitive data.

### Steps to Reproduce

1. An attacker can send a malicious certificate to the vulnerable server to establish a fake HTTPS connection.
2. The server will accept the invalid certificate and allow the request to proceed.
3. The attacker can then intercept or tamper with sensitive data being transmitted over the connection.

### Proof of Concept (PoC)

To demonstrate this vulnerability, an attacker could use the following Python script:

```python
import requests

target_url = "https://vulnerable-server.com"

search_customer_username = requests.post(
    target_url + '/search',
    json={'username': 'test'},
    proxies=None,
    headers={'Authorization': 'Bearer test_token'},
    verify=False
)

print(search_customer_username.status_code)
```
This script sends a POST request to the vulnerable server without verifying the SSL/TLS certificate, allowing an attacker to intercept or tamper with sensitive data.
