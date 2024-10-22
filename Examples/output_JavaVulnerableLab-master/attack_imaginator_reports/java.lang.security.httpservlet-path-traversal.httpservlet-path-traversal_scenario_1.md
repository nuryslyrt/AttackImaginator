
# Attack Imaginator Report - Scenario 1

Hi dear security enthusiast! (^^,)
I'm your fellow attack imaginator. I'll provide possible hacking scenarios over your code review findings.
Hope, they'll help you to test your systems and increase their security bar! 
Don't forget, I don't accept any responsibility in your actions.
Please examine the scenarios that I'll create properly for not causing any harm to your test scope.

## CODE REVIEW FINDING DETAILS:

**FINDING TITLE:**  

java.lang.security.httpservlet-path-traversal.httpservlet-path-traversal

### FINDING SEVERITY:

MEDIUM

### FINDING EXPLANATION:

Detected a potential path traversal. A malicious actor could control the location of this file, to include going backwards in the directory with '../'. To address this, ensure that user-controlled variables in file paths are sanitized. You may also consider using a utility method such as org.apache.commons.io.FilenameUtils.getName(...) to only retrieve the file name from the path.

### VULNERABLE CODE PATH:

/Users/USERNAME/Downloads/JavaVulnerableLab-master/src/main/java/org/cysecurity/cspf/jvl/controller/AddPage.java


### VULNERABLE CODE SNIPPET:


## ATTACK SCENARIO DETAILS:

### Impact

- Critical is not applicable here as this finding will allow a user to potentially navigate to different directories on the system.
- However, Medium is suitable for this scenario.

### Explanation

This Java-based application uses a `File` object with a user-controlled `filePath` variable. A malicious actor could potentially manipulate the value of `filePath` to include directory traversal attacks such as "../" or ".//". For example, if `filePath` is set to "/etc/passwd", the attacker could access sensitive files like `/etc/passwd`, `/etc/shadow`, or even `../etc/some-sensitive-file`. This allows an attacker to potentially access sensitive system files and data. To prevent this, it's essential to sanitize user-controlled variables in file paths using methods like `FilenameUtils.getName(...)`.

Here are some examples of directory traversal attacks:

- Accessing a file outside the intended path: `File f = new File("/etc/passwd");`
- Accessing a parent directory: `File f = new File("../etc/some-sensitive-file");`
- Accessing a sibling directory: `File f = new File("./some-other-directory/some-file");`

### Steps to Reproduce

1. **Reconstruct the file path**: Malicious actor must reconstruct the desired path by manipulating the user-controlled variable.
2. **Use directory traversal attacks**: The attacker could use directory traversal attacks such as "../" or ".//".
3. **Gain access to sensitive files**: The attacker could potentially access sensitive system files and data.

### Proof of Concept (PoC)

To demonstrate this vulnerability, you can use the following Java code:
```java
                File f = new File("/etc/passwd");
                System.out.println(f.exists());
                
                // Using directory traversal attack: '../'
                String filePath = "/etc/shadow";
                f = new File(filePath);
                System.out.println(f.exists());

                // Using directory traversal attack: './/'
                filePath = "./etc/some-sensitive-file";
                f = new File(filePath);
                System.out.println(f.exists());
```
