import json
import requests
import argparse

def get_git_events(user):
        url = f"https://api.github.com/users/{user}/events"
        response = requests.get(url)
        if response.status_code == 200:
            event_json = response.json()
            for event in event_json:
                if event["type"] == "CreateEvent" and event["payload"]["ref_type"] == "repository":
                    print(f'- Created { event["repo"]["name"]} {event["payload"]["ref_type"]}')
                elif event["type"] == "CreateEvent":
                    print(f'- Created { event["payload"]["ref"]} {event["payload"]["ref_type"]}')
                elif event["type"] == "PushEvent" and event["payload"]["commits"]:
                    num_of_commits = len(event["payload"]["commits"])
                    print(f'- Pushed {num_of_commits} commit to {event["repo"]["name"]}')
        else:
            print(f"failed {response.status_code}")

def main():
    # create a parser
    parser = argparse.ArgumentParser()
    
    parser.add_argument("name", type=str, help="Enter the github username") # this is a positional argument and they are required.
    
    args = parser.parse_args()
    if args.name:
        get_git_events(args.name)
        


if __name__ == "__main__":
    main()
    


