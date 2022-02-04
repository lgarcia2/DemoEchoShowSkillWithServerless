# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import json

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
import ask_sdk_core.utils as ask_utils
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model.interfaces.alexa.presentation.apl import (RenderDocumentDirective)

from ask_sdk_model import Response

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# APL Document file paths for use in handlers
hello_world_doc_path = "helloworldDocument.json"
# Tokens used when sending the APL directives
HELLO_WORLD_TOKEN = "helloworldToken"

def _load_apl_document(file_path):
    # type: (str) -> Dict[str, Any]
    """Load the apl json document at the path into a dict object."""
    with open(file_path) as f:
        return json.load(f)

class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        logging.info("Determining whether handling...")
        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logging.info("Handling...")
        supported_interfaces = ask_utils.request_util.get_supported_interfaces(handler_input)
        # If this device supports APL 
        # e.g. If this device is an Echo Show
        if supported_interfaces.alexa_presentation_apl is not None:
            logging.info('This device supports APL')
            #
            # Flag you can toggle based on where your APL is
            # This isnt production code, its just for demonstration purposes
            the_api_document_is_only_in_the_developer_console = True
            #
            # add "Alexa.Presentation.APL.RenderDocument" to the handler_input
            if the_api_document_is_only_in_the_developer_console:
                # if your APL is only in the console, load it from the console
                document_name = "ImageAPLDocument" # The name of the APL we saved
                token = document_name + "Token"
                # using an image api: https://picsum.photos/300/200
                # for more info see: https://picsum.photos/
                handler_input.response_builder.add_directive(
                    RenderDocumentDirective(
                        token=token,
                        document={
                            "src":'doc://alexa/apl/documents/' + document_name,
                            "type": "Link"
                        },
                        datasources={
                            "imageTemplateData": {
                                "type": "object",
                                "objectId": "imageSample",
                                "properties": {
                                    "backgroundImage": {
                                        "contentDescription": None,
                                        "smallSourceUrl": None,
                                        "largeSourceUrl": None,
                                        "sources": [
                                            {
                                                "url": "https://d2o906d8ln7ui1.cloudfront.net/images/templates_v3/gridlist/GridListBackground_Dark.png",
                                                "size": "large"
                                            }
                                        ]
                                    },
                                    "image": {
                                        "contentDescription": None,
                                        "smallSourceUrl": None,
                                        "largeSourceUrl": None,
                                        "sources": [
                                            {
                                                "url": "https://picsum.photos/300/200",
                                                "size": "large"
                                            }
                                        ]
                                    },
                                    "title": "Plant of the day",
                                    "logoUrl": "https://d2o906d8ln7ui1.cloudfront.net/images/templates_v3/logo/logo-modern-botanical-white.png"
                                }
                            }
                        }
                    )
                )
            else:
                # if your APL is alongside the code, load it from the package
                # NOTE: it must be in a specefic place (in the lambda folder)
                # see https://developer.amazon.com/en-US/docs/alexa/alexa-presentation-language/use-apl-with-ask-sdk.html 
                # for more detail
                handler_input.response_builder.add_directive(
                    RenderDocumentDirective(
                        token=HELLO_WORLD_TOKEN,
                        document=_load_apl_document()
                    )
                )
        else:
            logging.info('This device does not support APL. \r\n Supported Interfaces: \r\n {supported_interfaces}')
        #
        #
        speak_output = "Welcome, you can say Hello or Help. Which would you like to try?"
        #
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
    )


    # The old handler from earlier in the tutorial
    #def handle(self, handler_input):
    #    # type: (HandlerInput) -> Response
    #    logging.info("Handling...")
    #    supported_interfaces = ask_utils.request_util.get_supported_interfaces(handler_input)
    #    # If this device supports APL 
    #    # e.g. If this device is an Echo Show
    #    if supported_interfaces.alexa_presentation_apl is not None:
    #        logging.info('This device supports APL')
    #
    #        # Flag you can toggle based on where your APL is
    #        # This isnt production code, its just for demonstration purposes
    #        the_api_document_is_only_in_the_developer_console = True
    #
    #        # add "Alexa.Presentation.APL.RenderDocument" to the handler_input
    #        if the_api_document_is_only_in_the_developer_console:
    #            # if your APL is only in the console, load it from the console
    #            document_name = "HelloWorldDocument" # The name of the APL we saved
    #            token = document_name + "Token"
    #            handler_input.response_builder.add_directive(
    #                RenderDocumentDirective(
    #                    token=token,
    #                    document={
    #                        "src":'doc://alexa/apl/documents/' + document_name,
    #                        "type": "Link"
    #                    },
    #                    datasources={
    #                        "helloWorldDataSource":{
    #                            "title": "We did it!",
    #                            "subtitle": "Hello World is coming from code!",
    #                            "color": "@colorTeal800"
    #                        }
    #                    }
    #                )
    #            )
    #        else:
    #            # if your APL is alongside the code, load it from the package
    #            # NOTE: it must be in a specefic place (in the lambda folder)
    #            # see https://developer.amazon.com/en-US/docs/alexa/alexa-presentation-language/use-apl-with-ask-sdk.html 
    #            # for more detail
    #            handler_input.response_builder.add_directive(
    #                RenderDocumentDirective(
    #                    token=HELLO_WORLD_TOKEN,
    #                    document=_load_apl_document()
    #                )
    #            )
    #    else:
    #        logging.info('This device does not support APL. \r\n Supported Interfaces: \r\n {supported_interfaces}')
    #
    #
    #    speak_output = "Welcome, you can say Hello or Help. Which would you like to try?"
    #
    #    return (
    #        handler_input.response_builder
    #            .speak(speak_output)
    #            .ask(speak_output)
    #            .response
    #    )


class HelloWorldIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("HelloWorldIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Hello World!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "You can say hello to me! How can I help?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Goodbye!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response

class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.

logging.info("Something")

sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(HelloWorldIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

handler = sb.lambda_handler()
