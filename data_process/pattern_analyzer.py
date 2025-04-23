from core.llm_chat import LLMChat
from utils.logger_setup_data_extraction import logger
from prompt.generate_pattern_data import *
from core.context_manager import ContextManager

class LogicIdentifier:
    def __init__(self):        
        self.chat = LLMChat()
        
    def generate_unique_id(self, data):
        context_manager_frames = data
        context_manager_frames_new = ContextManager()

        for index, frame in enumerate(context_manager_frames.get_context()):
            if not frame:
                continue

            context_response = self.chat.context_respond_default(frame, GENERATE_UNIQUE_ID_REQUEST.format(id={index + 1}))
            context = context_response['answer'].replace("```json", '').replace("```", '')
            logger.info(f"response answer setting 'unique_id' and 'behavior_id':\n {context}")
            logger.info("=========2.AAAAAA===============")
            context_manager_frames_new.add_context(context)

        context_manager_frames_new.print_context()
        logger.info("=========2.BBBBBB===============")

        return context_manager_frames_new
    
    def merge_steps(self, data):
        # update each frame to add unidque_id, behavior_id
        context_manager_frames_new = self.generate_unique_id(data) 

        context_response = self.chat.context_respond_default(context_manager_frames_new.context_to_str(), MERGE_BEHAVIOR_ID_REQUEST)
        context = context_response['answer'].replace("```json", '').replace("```", '')
        logger.info(f"response answer for merge unique id':\n {context}")
        logger.info("=========2.CCCCCC===============")

        return context