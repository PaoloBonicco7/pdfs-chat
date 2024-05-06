from langchain_openai import ChatOpenAI
from langchain_community.llms import Ollama
from pydantic import ValidationError


def get_model(model_kind: str = "local", model_name: str = "phi-3"):
    """
    Get the model based on the provided model kind and model name.

    :param model_kind: The kind of the model to get. This can be either "local" or "openai".
                       If "local", an Ollama model is returned. If "openai", a ChatOpenAI model is returned.
                       Defaults to "local".
    :param model_name: The name of the model to get. If the model kind is "local", this should be the name of an Ollama model.
                       If the model kind is "openai", this should be the name of a ChatOpenAI model.
                       If not provided and the model kind is "openai", the model name defaults to "gpt-3.5-turbo".
    :return: The requested model. If the model kind or model name is invalid, a ValueError is raised.
    """
    if model_kind == "local":
        try:
            model = Ollama(model=model_name)
        except ValidationError:
            print("Invalid model name")
            raise ValueError("Invalid model name")

    elif model_kind == "openai":
        if model_name is None:
            model = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
        else:
            try:
                model = ChatOpenAI(model_name=model_name, temperature=0)
            except ValidationError:
                print("Invalid model name")
                raise ValueError("Invalid model name")
    else:
        raise ValueError("Invalid model kind")

    return model
