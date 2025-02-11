import clipboard
from .ocr_drivers import get_driver
from .behavior_context import MESSAGE_CONTEXT, Message, Prompt
from .ocr_drivers.base_driver import ClipboardContext


def create_message_context(prompt: str, args) -> list[dict[str, str]]:
    """An important part of a ChatBot is the prior context. Here, we carefully
    construct the context for the messages we are sending.

    This function returns an OpenAI-API ready message with the prompt included.
    :param prompt: The prompt for the chatbot
    :return: The API-ready message
    """
    if False:
        context: WindowContext = driver.extract_context()
    elif not args.no_clipboard:
        context: ClipboardContext = ClipboardContext(text=clipboard.paste())
    else:
        context = None
    
    new_context = MESSAGE_CONTEXT[:]
    new_context.append(
        Message(role="user", content=Prompt(context=context, prompt=prompt))
    )
    api_format = [m.to_api() for m in new_context]
    
    return api_format
