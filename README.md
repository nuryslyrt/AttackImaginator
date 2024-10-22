<h1 align="center">
  <img src="https://raw.githubusercontent.com/nuryslyrt/AttackImaginator/refs/heads/main/attackimaginator.png" alt="subfinder" width="400px">
  <br>
</h1>

<h4 align="center">LLM Supported Attack Scenario Creator from Code Review</h4>


<p align="center">
<a href="https://github.com/nuryslyrt/AttackImaginator/issues"><img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat"></a>
<a href="https://x.com/nuryslyrt"><img src="https://img.shields.io/twitter/follow/nuryslyrt.svg?logo=twitter"></a>
<a href="https://www.linkedin.com/in/nuryesilyurt"><img src="https://img.shields.io/badge/LinkedIn-blue?logo=linkedin&logoColor=white&style=for-the-bad"></a>
</p>

<p align="center">
  <a href="#features">Features</a> •
  <a href="#installation">Install</a> •
  <a href="#usage">Usage</a>
</p>

---

# AttackImaginator

Welcome to **AttackImaginator**—a project crafted entirely for educational purposes! Discover how you can leverage LLMs to enhance your day-to-day work quality and skills, instead of relying blindly on their output.

## What Does It Do?

AttackImaginator harnesses the power of **Semgrep** to scan your project using defined rule repositories. It then employs LLMs to generate possible attack scenarios, aiding security engineers in their learning and penetration tests.

Code review is a mighty tool in security testing that can unveil vulnerabilities without the need for exhaustive hours of testing. While it might seem daunting to newcomers in pentesting, the reality is that code review is your best friend!

AttackImaginator helps elevate your automated code review to the next level by creating applicable Proofs of Concept (PoCs) and explanations to share with your developer peers, partners, and more.

## Output of AttackImaginator

All outputs are generated based on the code repository you provide.

> **Disclaimer:** I do not accept any responsibility for your actions. Please thoroughly examine the scenarios that AttackImaginator creates to ensure they do not cause any harm outside your test scope.

## Installation

```
$ git clone https://github.com/nuryslyrt/AttackImaginator.git
$ cd AttackImaginator
$ python3 -m venv .venv
$ source .venv/bin/activate
$ python3 -m pip install -r requirements.txt
```

## Usage

```bash
$ python3 attack_imaginator.py -t [FULL_PATH_OF_THE_CODE_REPO_WILL_BE_SCANNED] -m [THE_MODEL_THAT_DEPLOYED_ON_YOUR_OLLAMA]
```
Check the scanned repo folder to find your outputs!

To see what they may look like, check the [example outputs](https://github.com/nuryslyrt/AttackImaginator/tree/main/Examples) from some known vulnerable apps!

![Example terminal](https://raw.githubusercontent.com/nuryslyrt/AttackImaginator/refs/heads/main/example_terminal_output.png)


## Features

**Automated Scanning:** Uses Semgrep to analyze your codebase with defined rule repositories. Semgrep is very powerful, lightweight and open source tool that I recommend everyone to create their own rules!

**LLM-Powered Scenarios:** Employs LLMs to imagine potential attack vectors based on your code.

**Educational Focus:** Aims to enhance your security testing skills in a fun and engaging way.




## Contribution

AttackImaginator is a passion project built entirely for fun!

Feel free to send a pull request to enhance it!

Here are some features you might contribute:

- Adding more model connections (e.g., AWS, Google, OpenAI)
- Remediation creation
- Scenario combination for better impact and attack analysis

---

Let's make security testing more imaginative and fun together! 🚀

-EOF
