
# Attack Imaginator Report

Hi dear security enthusiast! (^^,)
I'm your fellow attack imaginator. I'll provide possible hacking scenarios over your code review findings.
Hope, they'll help you to test your systems and increase their security bar! 
Don't forget, I don't accept any responsibility in your actions.
Please examine the scenarios that I'll create properly for not causing any harm to your test scope.


## CODE REVIEW FINDING DETAILS:

**FINDING TITLE:**  

python.flask.security.audit.render-template-string.render-template-string

### FINDING SEVERITY:

MEDIUM

### FINDING EXPLANATION:

Found a template created with string formatting. This is susceptible to server-side template injection and cross-site scripting attacks.

### VULNERABLE CODE PATH:

```
/Users/USERNAME/Downloads/Vulnerable-Flask-App-master/app/app.py
```

### VULNERABLE CODE SNIPPET:

```
                    return render_template_string(template, dir=dir, help=help, locals=locals), 404
```

## ATTACK SCENARIO DETAILS:


### Impact

None

### Explanation

None

### Steps to Reproduce

None

### Proof of Concept (PoC)

None
