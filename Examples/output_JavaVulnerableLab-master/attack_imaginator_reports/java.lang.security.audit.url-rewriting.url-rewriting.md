
# Attack Imaginator Report

Hi dear security enthusiast! (^^,)
I'm your fellow attack imaginator. I'll provide possible hacking scenarios over your code review findings.
Hope, they'll help you to test your systems and increase their security bar! 
Don't forget, I don't accept any responsibility in your actions.
Please examine the scenarios that I'll create properly for not causing any harm to your test scope.


## CODE REVIEW FINDING DETAILS:

**FINDING TITLE:**  

java.lang.security.audit.url-rewriting.url-rewriting

### FINDING SEVERITY:

MEDIUM

### FINDING EXPLANATION:

URL rewriting has significant security risks. Since session ID appears in the URL, it may be easily seen by third parties.

### VULNERABLE CODE PATH:

```
/Users/USERNAME/Downloads/JavaVulnerableLab-master/src/main/java/org/cysecurity/cspf/jvl/controller/XPathQuery.java
```

### VULNERABLE CODE SNIPPET:

```
    protected void processRequest(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");
        PrintWriter out = response.getWriter();
        try {
            String user=request.getParameter("username");
            String pass=request.getParameter("password");
            
            //XML Source:
            String XML_SOURCE=getServletContext().getRealPath("/WEB-INF/users.xml");
            
            //Parsing XML:
            DocumentBuilderFactory factory=DocumentBuilderFactory.newInstance();
            factory.setNamespaceAware(true);
            DocumentBuilder builder=factory.newDocumentBuilder();
            Document xDoc=builder.parse(XML_SOURCE);
            
            XPath xPath=XPathFactory.newInstance().newXPath();
            
            //XPath Query:
            String xPression="/users/user[username='"+user+"' and password='"+pass+"']/name";
            
            //running Xpath query:
            String name=xPath.compile(xPression).evaluate(xDoc);
            out.println(name);
            if(name.isEmpty())
            {
                response.sendRedirect(response.encodeURL("ForwardMe?location=/vulnerability/Injection/xpath_login.jsp?err=Invalid Credentials"));
            }
            else
            {
                 HttpSession session=request.getSession();
                 session.setAttribute("isLoggedIn", "1");
                  session.setAttribute("user", name);
                 response.sendRedirect(response.encodeURL("ForwardMe?location=/index.jsp"));                                  
            }
        } 
        catch(Exception e)
        {
            out.print(e);
        }        
        finally {
            out.close();
        }
    }
```

## ATTACK SCENARIO DETAILS:


### Impact

- Medium

### Explanation

The vulnerability in this code arises from the use of user input directly in an XPath query. This allows an attacker to manipulate the XPath expression and potentially access sensitive data or inject malicious requests.
 
                  An attacker could exploit this by providing a specially crafted username or password, allowing them to bypass authentication or gain unauthorized access to sensitive data.
                  The use of string concatenation to build the XPath query makes it vulnerable to injection attacks. An attacker could provide a username that includes characters with special meaning in XPath, such as the `%3A` character, which would allow them to filter out specific users or even inject malicious requests.

### Steps to Reproduce

- The attacker would start by sending a request to the login page with a specially crafted username and password that includes malicious characters.
                     - The server would process the request and build the XPath query using the provided user input.
                     - The malicious character(s) in the username would be interpreted as part of the XPath expression, potentially allowing the attacker to bypass authentication or access sensitive data.
                     - Alternatively, the attacker could inject malicious requests by providing a username that includes special characters that can be used to manipulate the XPath query.

### Proof of Concept (PoC)

To demonstrate this vulnerability, an attacker could use the following modified request:
 
                     ```
                     GET /login HTTP/1.1
                     Host: example.com
                     Content-Type: application/x-www-form-urlencoded
 
                     username=%3Cscript>alert('XSS')
