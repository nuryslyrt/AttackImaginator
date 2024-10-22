
# Attack Imaginator Report - Scenario 2

Hi dear security enthusiast! (^^,)
I'm your fellow attack imaginator. I'll provide possible hacking scenarios over your code review findings.
Hope, they'll help you to test your systems and increase their security bar! 
Don't forget, I don't accept any responsibility in your actions.
Please examine the scenarios that I'll create properly for not causing any harm to your test scope.

## CODE REVIEW FINDING DETAILS:

**FINDING TITLE:**  

java.lang.security.audit.cookie-missing-secure-flag.cookie-missing-secure-flag

### FINDING SEVERITY:

LOW

### FINDING EXPLANATION:

A cookie was detected without setting the 'secure' flag. The 'secure' flag for cookies prevents the client from transmitting the cookie over insecure channels such as HTTP. Set the 'secure' flag by calling 'password.setSecure(true);'

### VULNERABLE CODE PATH:

/Users/USERNAME/Downloads/JavaVulnerableLab-master/src/main/java/org/cysecurity/cspf/jvl/controller/LoginValidator.java


### VULNERABLE CODE SNIPPET:


## ATTACK SCENARIO DETAILS:

### Impact

- High impact symbolizes relatively exploitable scenarios. Relatively exploitable scenarios require a user authorization to run the exploit scenario. However, the scenario shouldn't be hard to exploit or return something critical as output when it's exploited.This vulnerability is still exploitable if an attacker knows where to look for the cookie in the request headers.While this vulnerability is not as severe as a Critical impact scenario, it can still be exploitable with some knowledge of HTTP requests and headers. To exploit this scenario, an attacker would need to manually inspect the HTTP request headers to find the cookie value.1. Inspect the HTTP request headers for the cookie
2. Use the cookie value to send a new request to gain accessTo demonstrate this vulnerability, we can use the `curl` command-line tool to inspect the HTTP request headers and extract the cookie value.
```bash
   curl -i -H "Cookie: session_id=12345" https://example.com/protected
```

### Explanation

While this vulnerability is not as severe as a Critical impact scenario, it can still be exploitable with some knowledge of HTTP requests and headers. To exploit this scenario, an attacker would need to manually inspect the HTTP request headers to find the cookie value.

### Steps to Reproduce

1. Inspect the HTTP request headers for the cookie
   2. Use the cookie value to send a new request to gain access

### Proof of Concept (PoC)

To demonstrate this vulnerability, we can use the `curl` command-line tool to inspect the HTTP request headers and extract the cookie value.
```bash
   curl -i -H "Cookie: session_id=12345" https://example.com/protected
```
