import sys
from data_process.concept_analyzer import ConceptAnalyzer
from data_process.pattern_analyzer import LogicIdentifier
from data_process.knowledge_generator import KnowledgeGenerator
from utils.logger_setup_data_extraction import logger


def run():
    logger.info(f"started...")    
    
    # Step1: Generate concept data
    logger.info(f"\nstarted ConceptAnalyzer...")       
    concept_analyzer = ConceptAnalyzer()
    concept_data = concept_analyzer.generate_concept_data()
    logger.info(f"end ConceptAnalyzer...\n")

    '''    
    # Step2: Merge same steps and compound steps
    logger.info(f"\nstarted LogicIdentifier...") 
    logic_identifier = LogicIdentifier()
    pattern_data = logic_identifier.merge_steps(concept_data)
    print("Pattern Data:", pattern_data)
    logger.info(f"end LogicIdentifier...\n") '
    '''
    


    # Step3: Generate knowledge JSON
    logger.info(f"\nstarted KnowledgeGenerator...") 
    context_manager_frames = concept_data
    knowledge_generator = KnowledgeGenerator()
    knowledge_json = knowledge_generator.generate_knowledge_json(context_manager_frames)
    print("Knowledge Data:", knowledge_json)
    logger.info(f"end KnowledgeGenerator...\n")


if __name__ == "__main__":
    run()