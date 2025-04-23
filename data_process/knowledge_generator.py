from utils.logger_setup_data_extraction import logger
from prompt.generate_knowledge_json import *
from core.llm_chat import LLMChat
from core.context_manager import ContextManager

class KnowledgeGenerator:
    def __init__(self):        
        self.chat = LLMChat()
    
    def generate_knowledge_json(self, data):
        context_manager_frames_partial = ContextManager()

        context_manager_frames = data
        for frame in context_manager_frames.get_context():
            print(frame)
            context_response = self.chat.context_respond_default(frame, EXTRACT_STEP_DESC_STATE_TRANS)
            context = context_response['answer'].replace("```json", '').replace("```", '')
            logger.info(f"response answer for extract 'action_description' and 'state_transition_caption':\n {context}")
            logger.info("=========3.AAAAAA===============")
            context_manager_frames_partial.add_context(context)

        context_response = self.chat.context_respond_default(context_manager_frames_partial.context_to_str(), GENERATE_BUSINESS_FLOW_REQUEST)
        context = context_response['answer'].replace("```json", '').replace("```", '')
        logger.info(f"response answer for generate business flow:\n {context}")
        logger.info("=========3.BBBBBB===============")

        '''        
        context_response = self.chat.context_respond_default(context_manager_frames.context_to_str(), GENERATE_BUSINESS_FLOW_REQUEST)
        context = context_response['answer'].replace("```json", '').replace("```", '')
        logger.info(f"response answer for generate business flow:\n {context}")
        logger.info("=========3.BBBBBB===============")
        '''

        context_manager_frames.add_context(context)
        context_manager_frames.print_context()

        context_response = self.chat.context_respond_default(context_manager_frames.context_to_str(), COMPILE_KNOWLEDGE_JSON_REQUEST)
        context = context_response['answer'].replace("```json", '').replace("```", '')
        logger.info(f"response answer for generate knowledge json:\n {context}")
        logger.info("=========3.CCCCCC===============")
        
        return context