import requests
import argparse


def parse_events(event: dict) -> None:
    if event["type"] == "CreateEvent" and event["payload"]["ref_type"] == "repository":
        print(f'- Created { event["repo"]["name"]} {event["payload"]["ref_type"]}')
    elif event["type"] == "CreateEvent":
        print(f'- Created { event["payload"]["ref"]} {event["payload"]["ref_type"]}')
    elif event["type"] == "PushEvent" and event["payload"]["commits"]:
        num_of_commits = len(event["payload"]["commits"])
        print(f'- Pushed {num_of_commits} commit to {event["repo"]["name"]}')
    
def get_git_events(user: str, event_per_page: int = 10) -> None:
        url = f"https://api.github.com/users/{user}/events"
        page_number = 1
        while True:
            params = {"page": page_number, "per_page": event_per_page}
            response = requests.get(url, params=params)
            if response.status_code == 200:
                event_json = response.json()
                if not event_json:
                    break
                for event in event_json:
                    parse_events(event)
            else:
                print(f"failed {response.status_code}")
            page_number += 1



def main():
    # create a parser
    parser = argparse.ArgumentParser()
    
    parser.add_argument("name", type=str, help="Enter the github username") # this is a positional argument and they are required.
    
    args = parser.parse_args()
    if args.name:
        get_git_events(args.name)
        

if __name__ == "__main__":
    main()
    


