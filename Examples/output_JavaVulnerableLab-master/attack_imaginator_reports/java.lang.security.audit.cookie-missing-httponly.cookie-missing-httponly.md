
# Attack Imaginator Report

Hi dear security enthusiast! (^^,)
I'm your fellow attack imaginator. I'll provide possible hacking scenarios over your code review findings.
Hope, they'll help you to test your systems and increase their security bar! 
Don't forget, I don't accept any responsibility in your actions.
Please examine the scenarios that I'll create properly for not causing any harm to your test scope.


## CODE REVIEW FINDING DETAILS:

**FINDING TITLE:**  

java.lang.security.audit.cookie-missing-httponly.cookie-missing-httponly

### FINDING SEVERITY:

LOW

### FINDING EXPLANATION:

A cookie was detected without setting the 'HttpOnly' flag. The 'HttpOnly' flag for cookies instructs the browser to forbid client-side scripts from reading the cookie. Set the 'HttpOnly' flag by calling 'cookie.setHttpOnly(true);'

### VULNERABLE CODE PATH:

```
/Users/USERNAME/Downloads/JavaVulnerableLab-master/src/main/java/org/cysecurity/cspf/jvl/controller/LoginValidator.java
```

### VULNERABLE CODE SNIPPET:

```
                                        response.addCookie(password);
```

## ATTACK SCENARIO DETAILS:


### Impact

- High

### Explanation

The code in the LoginValidator.java file is adding a cookie named "password" to the response without setting the 'HttpOnly' flag. This allows an attacker who has access to the client-side scripts (e.g., JavaScript) to read the password cookie, potentially leading to unauthorized access to the application.

When a user logs in with a password, it is stored in a cookie on the client-side. If an attacker can access this cookie, they may be able to obtain the password and use it to gain unauthorized access to the application.

### Steps to Reproduce

- An attacker discovers that the "password" cookie is not set with the 'HttpOnly' flag.
- The attacker uses JavaScript to inspect the response headers from the login request.
- The attacker uses the retrieved cookie value to make a subsequent request to the application, attempting to exploit the lack of the 'HttpOnly' flag.
- If successful, the attacker gains unauthorized access to the application using the stolen password.

### Proof of Concept (PoC)

To demonstrate this scenario, you can use the following JavaScript code to retrieve and log the value of the "password" cookie:
                     
```javascript
                     var xhr = new XMLHttpRequest();
                     xhr.open('GET', '/', true);
                     xhr.setRequestHeader('Cookie', 'password=');
                     xhr.send();
                     var password = xhr.responseText;
                     console.log(password);
```
                     
To prevent this scenario, you can set the 'HttpOnly' flag on the "password" cookie by calling `cookie.setHttpOnly(true);` as suggested in the finding explanation.
