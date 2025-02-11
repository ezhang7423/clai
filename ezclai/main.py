from argparse import ArgumentParser

from .api import initialize_api
from .message_creation import create_message_context


def main() -> None:
    parser = ArgumentParser("ezclai- your own command line AI!")
    parser.add_argument("prompt", type=str, nargs="+")
    # parser.add_argument("-m", "--model", default="gpt-3.5-turbo")
    parser.add_argument("-m", "--model", default="gpt-4")
    parser.add_argument("-c", "--no-clipboard", action="store_true")
    args = parser.parse_args()

    openai = initialize_api()

    prompt = " ".join(args.prompt)
    response = openai.ChatCompletion.create(
        model=args.model,
        messages=create_message_context(prompt, args),
    )

    best_response = response["choices"][0]["message"]["content"]
    print(best_response)
