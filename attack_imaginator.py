from semgrep_parser import SemgrepParser
from scenario_creator import ScenarioCreator
import argparse

def main(targetfolder, model):
    semgreper = SemgrepParser(target_directory=targetfolder)
    findings = semgreper.semgrep_scan()

    for finding in findings:
        ScenarioCreator(model=model, finding=finding, target_directory=targetfolder).scenario_reporter()

if __name__ == "__main__":
    print('''
   ▄████████     ███         ███        ▄████████  ▄████████    ▄█   ▄█▄       ▄█    ▄▄▄▄███▄▄▄▄      ▄████████    ▄██████▄   ▄█  ███▄▄▄▄      ▄████████     ███      ▄██████▄     ▄████████ 
  ███    ███ ▀█████████▄ ▀█████████▄   ███    ███ ███    ███   ███ ▄███▀      ███  ▄██▀▀▀███▀▀▀██▄   ███    ███   ███    ███ ███  ███▀▀▀██▄   ███    ███ ▀█████████▄ ███    ███   ███    ███ 
  ███    ███    ▀███▀▀██    ▀███▀▀██   ███    ███ ███    █▀    ███▐██▀        ███▌ ███   ███   ███   ███    ███   ███    █▀  ███▌ ███   ███   ███    ███    ▀███▀▀██ ███    ███   ███    ███ 
  ███    ███     ███   ▀     ███   ▀   ███    ███ ███         ▄█████▀         ███▌ ███   ███   ███   ███    ███  ▄███        ███▌ ███   ███   ███    ███     ███   ▀ ███    ███  ▄███▄▄▄▄██▀ 
▀███████████     ███         ███     ▀███████████ ███        ▀▀█████▄         ███▌ ███   ███   ███ ▀███████████ ▀▀███ ████▄  ███▌ ███   ███ ▀███████████     ███     ███    ███ ▀▀███▀▀▀▀▀   
  ███    ███     ███         ███       ███    ███ ███    █▄    ███▐██▄        ███  ███   ███   ███   ███    ███   ███    ███ ███  ███   ███   ███    ███     ███     ███    ███ ▀███████████ 
  ███    ███     ███         ███       ███    ███ ███    ███   ███ ▀███▄      ███  ███   ███   ███   ███    ███   ███    ███ ███  ███   ███   ███    ███     ███     ███    ███   ███    ███ 
  ███    █▀     ▄████▀      ▄████▀     ███    █▀  ████████▀    ███   ▀█▀      █▀    ▀█   ███   █▀    ███    █▀    ████████▀  █▀    ▀█   █▀    ███    █▀     ▄████▀    ▀██████▀    ███    ███ 
                                                               ▀                                                                                                                  ███    ███ 
    '''
    )
    

    EXAMPLE_USAGE = '''
        Example Usage:
        python3 attack_imaginator.py \
        -t TARGET_FOLDER_TO_SCAN \
        -m MODEL_IN_OLLAMA \
    '''

    parser = argparse.ArgumentParser(description='ATTACK IMAGINATOR')
    parser.add_argument('-t', '--targetfolder', type=str, help='Target folder to scan', required=True)
    parser.add_argument('-m', '--model', type=str, help='Model to call from ollama', required=True)

    # Parse arguments
    args = parser.parse_args()
    main(targetfolder=args.targetfolder, model=args.model)


