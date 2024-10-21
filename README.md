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
$ python3 -m venv .venv
$ source .venv/bin/activate
$ python3 -m pip install -r requirements.txt
```

## Execution

```bash
python3 attack_imaginator.py -t [FULL_PPATH_OF_THE_CODE_REPO_WILLBE_SCANNED] -m [THE_MODEL_THAT_DEPLOYED_ON_YOUR_OLLAMA]
```

PS: Check examples folder to see what kind of output you may see! 

## Contribution

AttackImaginator is a passion project built entirely for fun!

Feel free to send a pull request to enhance it!

Here are some features you might contribute:

- Adding more model connections (e.g., AWS, Google, OpenAI)
- Remediation creation
- Scenario combination for better impact and attack analysis

---

Let's make security testing more imaginative and fun together!

-EOF